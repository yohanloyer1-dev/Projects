import { readFileSync, writeFileSync } from 'fs';
import readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function question(query) {
  return new Promise(resolve => rl.question(query, resolve));
}

console.log('\n' + '='.repeat(60));
console.log('Gorgias Bulk Action Creator - Setup');
console.log('='.repeat(60) + '\n');

async function setup() {
  console.log('This will help you configure the bulk action creator.\n');

  // Step 1: Get store name
  console.log('STEP 1: Find Your Store Name');
  console.log('----------------------------');
  console.log('1. Open Gorgias in Chrome');
  console.log('2. Look at the URL: https://{YOUR-STORE}.gorgias.com/');
  console.log('   Example: https://fraserdemo1.gorgias.com/');
  console.log('   Store name would be: "fraserdemo1"\n');

  const storeName = await question('Enter your store name: ');

  if (!storeName || storeName.trim() === '') {
    console.log('\nError: Store name is required!');
    rl.close();
    process.exit(1);
  }

  // Step 2: Get auth token
  console.log('\n\nSTEP 2: Get Your Auth Token');
  console.log('----------------------------');
  console.log('1. Open Gorgias in Chrome');
  console.log('2. Press F12 to open DevTools');
  console.log('3. Go to "Network" tab');
  console.log('4. Click on any action in Gorgias (refresh the page if needed)');
  console.log('5. Find a request to "api.gorgias.work"');
  console.log('6. Click on it, scroll to "Request Headers"');
  console.log('7. Copy the ENTIRE "authorization" header value');
  console.log('   (starts with "Bearer eyJ...")');
  console.log('\nNOTE: This token will expire. You may need to re-run setup later.\n');

  const authToken = await question('Paste your auth token: ');

  if (!authToken || !authToken.startsWith('Bearer ')) {
    console.log('\nError: Invalid token! Make sure you copied the full "Bearer ..." value.');
    rl.close();
    process.exit(1);
  }

  // Save config
  const configContent = `// Auto-generated configuration
// Run 'npm run setup' to regenerate

export const CONFIG = {
  storeName: '${storeName.trim()}',
  authToken: '${authToken.trim()}',
  apiBase: 'https://api.gorgias.work'
};
`;

  writeFileSync('./config.js', configContent);

  console.log('\n' + '='.repeat(60));
  console.log('✓ Configuration saved to config.js');
  console.log('='.repeat(60));
  console.log('\nNext steps:');
  console.log('1. Edit actions-config.json with your actions');
  console.log('   OR use CSV: npm run csv actions.csv');
  console.log('2. Run: npm start');
  console.log('\n');

  rl.close();
}

setup().catch(console.error);
