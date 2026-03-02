const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

async function main() {
  const url = process.env.PAGES_URL || 'https://realagiorganization.github.io/royalvnc-demo/';
  const output = process.env.SCREENSHOT_PATH || path.join('docs', 'pages.png');

  fs.mkdirSync(path.dirname(output), { recursive: true });

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(url, { waitUntil: 'networkidle', timeout: 60000 });
  await page.screenshot({ path: output, fullPage: true });
  await browser.close();
  console.log(`Saved screenshot to ${output}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
