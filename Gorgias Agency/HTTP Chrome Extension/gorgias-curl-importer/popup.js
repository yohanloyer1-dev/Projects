document.getElementById('importBtn').addEventListener('click', async () => {
  const curlCommand = document.getElementById('curlInput').value.trim();
  const statusDiv = document.getElementById('status');
  const importBtn = document.getElementById('importBtn');

  if (!curlCommand) {
    showStatus('Please paste a curl command', 'error');
    return;
  }

  try {
    importBtn.disabled = true;
    showStatus('Parsing curl command...', 'success');

    const parsed = parseCurl(curlCommand);

    // Debug: log what we parsed
    console.log('Parsed curl:', parsed);

    // Send to content script
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    if (!tab.url.includes('gorgias.com')) {
      showStatus('Please open a Gorgias page first', 'error');
      importBtn.disabled = false;
      return;
    }

    // Inject content script if not already present
    try {
      await chrome.scripting.executeScript({
        target: { tabId: tab.id },
        files: ['content.js']
      });
    } catch (e) {
      // Content script might already be loaded, continue
      console.log('Content script injection:', e.message);
    }

    // Small delay to ensure content script is ready
    await new Promise(resolve => setTimeout(resolve, 100));

    chrome.tabs.sendMessage(tab.id, {
      action: 'populateForm',
      data: parsed
    }, (response) => {
      if (chrome.runtime.lastError) {
        showStatus('Error: ' + chrome.runtime.lastError.message, 'error');
        importBtn.disabled = false;
        return;
      }

      if (response && response.success) {
        showStatus('Successfully imported!', 'success');
        setTimeout(() => {
          window.close();
        }, 1500);
      } else {
        showStatus('Error: ' + (response?.error || 'Unknown error'), 'error');
        importBtn.disabled = false;
      }
    });

  } catch (error) {
    showStatus('Error parsing curl: ' + error.message, 'error');
    importBtn.disabled = false;
  }
});

function showStatus(message, type) {
  const statusDiv = document.getElementById('status');
  statusDiv.textContent = message;
  statusDiv.className = 'status ' + type;
  statusDiv.style.display = 'block';
}

function parseCurl(curlCommand) {
  const result = {
    method: 'GET',
    url: '',
    headers: [],
    body: null
  };

  // Remove 'curl' command at the start
  let command = curlCommand.trim();
  if (command.startsWith('curl')) {
    command = command.substring(4).trim();
  }

  // Extract method
  const methodMatch = command.match(/(?:--request|-X)\s+(\w+)/);
  if (methodMatch) {
    result.method = methodMatch[1].toUpperCase();
    command = command.replace(methodMatch[0], '');
  }

  // Extract URL (look for --url flag with optional quotes)
  const urlMatch = command.match(/--url\s+['"]?([^\s'"]+)['"]?/);
  if (urlMatch) {
    result.url = urlMatch[1];
    command = command.replace(urlMatch[0], '');
  } else {
    // Try to find URL as first argument (without --url)
    const directUrlMatch = command.match(/^\s*['"]?(https?:\/\/[^\s'"]+)['"]?/);
    if (directUrlMatch) {
      result.url = directUrlMatch[1];
      command = command.replace(directUrlMatch[0], '');
    }
  }

  // Extract headers
  const headerRegex = /(?:--header|-H)\s+['"]([^'"]+)['"]/g;
  let headerMatch;
  while ((headerMatch = headerRegex.exec(command)) !== null) {
    const headerLine = headerMatch[1];
    const colonIndex = headerLine.indexOf(':');
    if (colonIndex > 0) {
      const key = headerLine.substring(0, colonIndex).trim();
      const value = headerLine.substring(colonIndex + 1).trim();
      result.headers.push({ key, value });
    }
  }

  // Extract body/data - handle multiline with single quotes
  const dataMatch = command.match(/(?:--data|-d)\s+'\s*([\s\S]*?)\s*'/);
  if (dataMatch) {
    result.body = dataMatch[1].trim();
  } else {
    // Try double quotes
    const dataMatchDouble = command.match(/(?:--data|-d)\s+"\s*([\s\S]*?)\s*"/);
    if (dataMatchDouble) {
      result.body = dataMatchDouble[1].trim();
    }
  }

  return result;
}
