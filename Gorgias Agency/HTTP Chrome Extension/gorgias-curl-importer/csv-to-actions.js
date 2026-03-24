import { readFileSync, writeFileSync } from 'fs';

/**
 * Converts CSV to actions-config.json format
 *
 * CSV Format:
 * name,description,requestName,url,method,headers,requiresConfirmation
 *
 * Example:
 * Check Order,Get order status,Get Order,https://api.example.com/orders,GET,{"auth":"Bearer token"},false
 */

function parseCSV(csvContent) {
  const lines = csvContent.trim().split('\n');

  if (lines.length < 2) {
    throw new Error('CSV must have at least a header row and one data row');
  }

  const headers = lines[0].split(',').map(h => h.trim());
  const actions = [];

  // Validate required headers
  const required = ['name', 'description', 'url'];
  for (const field of required) {
    if (!headers.includes(field)) {
      throw new Error(`Missing required column: ${field}`);
    }
  }

  for (let i = 1; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line) continue; // Skip empty lines

    const values = parseCSVLine(line);
    const action = {};

    headers.forEach((header, index) => {
      const value = values[index]?.trim() || '';

      switch(header) {
        case 'name':
          action.name = value;
          break;
        case 'description':
          action.description = value;
          break;
        case 'requestName':
          action.requestName = value || action.name; // Default to name if empty
          break;
        case 'url':
          action.url = value;
          break;
        case 'method':
          action.method = value || 'GET';
          break;
        case 'headers':
          try {
            action.headers = value ? JSON.parse(value) : {};
          } catch (e) {
            console.warn(`Warning: Invalid JSON in headers for action "${action.name}". Using empty object.`);
            action.headers = {};
          }
          break;
        case 'requiresConfirmation':
          action.requiresConfirmation = value.toLowerCase() === 'true';
          break;
      }
    });

    // Set defaults
    if (!action.requestName) action.requestName = action.name;
    if (!action.method) action.method = 'GET';
    if (!action.headers) action.headers = {};
    if (action.requiresConfirmation === undefined) action.requiresConfirmation = false;

    actions.push(action);
  }

  return { actions };
}

/**
 * Parses a CSV line, handling quoted values with commas
 */
function parseCSVLine(line) {
  const values = [];
  let current = '';
  let inQuotes = false;

  for (let i = 0; i < line.length; i++) {
    const char = line[i];

    if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === ',' && !inQuotes) {
      values.push(current);
      current = '';
    } else {
      current += char;
    }
  }

  values.push(current);
  return values;
}

// CLI usage
const csvFile = process.argv[2];

if (!csvFile) {
  console.log('Usage: node csv-to-actions.js <csv-file>');
  console.log('\nCSV Format:');
  console.log('name,description,requestName,url,method,headers,requiresConfirmation');
  console.log('\nExample:');
  console.log('Check Order,Get order status,Get Order,https://api.example.com/orders,GET,"{\\"auth\\":\\"Bearer token\\"}",false');
  process.exit(1);
}

try {
  const csvContent = readFileSync(csvFile, 'utf8');
  const config = parseCSV(csvContent);

  const outputFile = 'actions-config.json';
  writeFileSync(outputFile, JSON.stringify(config, null, 2));

  console.log(`✓ Converted ${config.actions.length} actions from CSV`);
  console.log(`✓ Saved to ${outputFile}`);
  console.log('\nNext step: Run "npm start" to create these actions in Gorgias');
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exit(1);
}

export { parseCSV };
