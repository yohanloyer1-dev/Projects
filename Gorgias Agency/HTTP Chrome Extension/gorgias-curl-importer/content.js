// Prevent multiple injections
if (window.gorgiasContentScriptLoaded) {
  console.log('Content script already loaded, skipping');
} else {
  window.gorgiasContentScriptLoaded = true;

  // Listen for messages from the popup
  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'populateForm') {
      try {
        populateGorgiasForm(request.data);
        sendResponse({ success: true });
      } catch (error) {
        console.error('Error populating form:', error);
        sendResponse({ success: false, error: error.message });
      }
    }
    return true; // Keep message channel open for async response
  });
}

function populateGorgiasForm(data) {
  const { method, url, headers, body } = data;

  console.log('Populating Gorgias form with:', data);

  // 1. Set Request Name (derive from URL endpoint)
  const requestNameInput = document.querySelector('input[name="input-text-1074"]') ||
                           document.querySelector('input[maxlength="100"]');
  if (requestNameInput) {
    let endpointName = 'API Request';
    try {
      const urlPath = new URL(url).pathname;
      endpointName = urlPath.split('/').filter(Boolean).pop() || 'API Request';
    } catch (e) {
      // If URL parsing fails, try to extract endpoint from path
      const pathMatch = url.match(/\/([^/?]+)(?:\?|$)/);
      if (pathMatch) {
        endpointName = pathMatch[1];
      }
    }
    requestNameInput.value = endpointName;
    requestNameInput.dispatchEvent(new Event('input', { bubbles: true }));
    requestNameInput.dispatchEvent(new Event('change', { bubbles: true }));
  }

  // 2. Set URL (Draft.js editor)
  const urlEditor = document.querySelector('.TextInputWithVariables--editor--ag3a4 .public-DraftEditor-content');
  if (urlEditor) {
    console.log('Found URL editor, setting URL:', url);
    setDraftJsValue(urlEditor, url);
  } else {
    console.error('Could not find URL editor');
    console.log('Looking for selector: .TextInputWithVariables--editor--ag3a4 .public-DraftEditor-content');
  }

  // 3. Skip method automation - user must set manually
  // Just add headers and body
  if (headers && headers.length > 0) {
    addHeadersSequentially(headers, 0, body);
  } else if (body) {
    // No headers, just body
    setTimeout(() => {
      setRequestBody(body);
      setTimeout(cleanupAfterPopulation, 200);
    }, 300);
  } else {
    // No headers or body, just cleanup
    setTimeout(cleanupAfterPopulation, 300);
  }
}

// Function to set request body
function setRequestBody(body) {
  console.log('Setting request body...');

  // Find the body field - it should be in a section labeled "Body" or after headers
  const bodySection = Array.from(document.querySelectorAll('.NodeEditor--formField--UX6vV'))
    .find(field => {
      const label = field.querySelector('label');
      return label && (label.textContent.includes('Body') || label.textContent.includes('body'));
    });

  if (bodySection) {
    const bodyEditor = bodySection.querySelector('.DraftEditor-root .public-DraftEditor-content');
    if (bodyEditor) {
      console.log('Found body editor, setting content');
      setDraftJsValue(bodyEditor, body);
      console.log('Body set successfully');
    } else {
      console.error('Could not find body editor in body section');
    }
  } else {
    console.error('Could not find body section');
    console.log('Available sections:', document.querySelectorAll('.NodeEditor--formField--UX6vV'));
  }
}

// Recursive function to add headers one at a time with proper timing
function addHeadersSequentially(headers, index, body) {
  if (index >= headers.length) {
    console.log('All headers added');

    // After all headers are added, set the body if present
    if (body) {
      setTimeout(() => {
        setRequestBody(body);
        setTimeout(cleanupAfterPopulation, 200);
      }, 300);
    } else {
      // No body, just cleanup
      setTimeout(cleanupAfterPopulation, 200);
    }
    return;
  }

  const header = headers[index];
  console.log(`Adding header ${index + 1}/${headers.length}:`, header.key, '=', header.value);

  // Find and click Add Header button
  const addHeaderButton = Array.from(document.querySelectorAll('button')).find(btn =>
    btn.textContent.includes('Add Header')
  );

  if (!addHeaderButton) {
    console.error('Add Header button not found');
    return;
  }

  // Find the Headers section
  const headersSection = Array.from(document.querySelectorAll('.NodeEditor--formField--UX6vV'))
    .find(field => {
      const label = field.querySelector('label');
      return label && label.textContent.includes('Headers');
    });

  if (!headersSection) {
    console.error('Headers section not found');
    return;
  }

  // Count existing rows before clicking
  const beforeCount = headersSection.querySelectorAll('.NodeEditor--keyValueRow--jCWEm').length;

  // Click to add new header row
  addHeaderButton.click();

  // Wait for new inputs to appear with multiple attempts
  let attempts = 0;
  const maxAttempts = 10;

  const checkForInputs = () => {
    attempts++;

    // Look for key-value rows
    const keyValueRows = headersSection.querySelectorAll('.NodeEditor--keyValueRow--jCWEm');
    const rowCount = keyValueRows.length;

    console.log(`Attempt ${attempts}: Row count: ${beforeCount} -> ${rowCount}`);

    // Check if a new row was added
    if (rowCount > beforeCount) {
      // Get the last row (the newly added one)
      const lastRow = keyValueRows[keyValueRows.length - 1];

      // Find key input (regular input)
      const keyInput = lastRow.querySelector('.TextInput--input--OTqEq');

      // Find value editor (Draft.js editor)
      const valueEditor = lastRow.querySelector('.TextInputWithVariables--editor--ag3a4 .public-DraftEditor-content');

      if (keyInput && valueEditor) {
        console.log('Found key input and value editor');
        console.log('Key input:', keyInput);
        console.log('Value editor:', valueEditor);

        // Set key (regular input)
        setInputValue(keyInput, header.key);

        // Set value (Draft.js editor)
        setDraftJsValue(valueEditor, header.value);

        console.log('Set header:', header.key, '=', header.value);

        // Wait a bit before adding the next header
        setTimeout(() => {
          addHeadersSequentially(headers, index + 1, body);
        }, 150);
      } else {
        console.error('Could not find key input or value editor in row');
        if (attempts < maxAttempts) {
          setTimeout(checkForInputs, 100);
        }
      }
    } else if (attempts < maxAttempts) {
      // Try again in 100ms
      setTimeout(checkForInputs, 100);
    } else {
      console.error('Failed to find new row after', maxAttempts, 'attempts');
      console.log('Key-value rows:', keyValueRows);
    }
  };

  // Start checking for inputs
  setTimeout(checkForInputs, 100);
}

function setInputValue(input, value) {
  input.value = value;
  input.dispatchEvent(new Event('input', { bubbles: true }));
  input.dispatchEvent(new Event('change', { bubbles: true }));
  input.dispatchEvent(new Event('blur', { bubbles: true }));
}

// Helper function to set Draft.js editor values using clipboard
function setDraftJsValue(editor, value) {
  console.log('setDraftJsValue called with value:', value);

  editor.focus();

  // Use a simulated paste event which Draft.js handles natively
  // This keeps Draft.js internal state in sync
  const clipboardData = new DataTransfer();
  clipboardData.setData('text/plain', value);

  const pasteEvent = new ClipboardEvent('paste', {
    bubbles: true,
    cancelable: true,
    clipboardData: clipboardData
  });

  // Dispatch the paste event - Draft.js should handle this and update its internal state
  editor.dispatchEvent(pasteEvent);
  console.log('Paste event dispatched');

  // Trigger blur to finalize
  setTimeout(() => {
    editor.blur();
    console.log('Editor blurred, value should be set');
  }, 50);
}

// Cleanup function to reset focus and selection state
function cleanupAfterPopulation() {
  console.log('Running cleanup to reset focus and selection state...');

  // Clear any document selection
  if (window.getSelection) {
    window.getSelection().removeAllRanges();
  }

  // Blur any focused element
  if (document.activeElement) {
    document.activeElement.blur();
  }

  // Blur all Draft.js editors to ensure they release keyboard control
  const allEditors = document.querySelectorAll('.public-DraftEditor-content');
  allEditors.forEach(editor => {
    editor.blur();
  });

  // Click on a neutral element (the body) to reset focus
  document.body.click();

  console.log('Cleanup complete - keyboard input should be restored');
}
