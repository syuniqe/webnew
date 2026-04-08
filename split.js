const fs = require('fs');
const path = require('path');

const srcPath = 'C:\\Users\\Harsh\\Downloads\\index (1).html';
const targetDir = 'C:\\Users\\Harsh\\.gemini\\antigravity\\scratch\\syuniqe-enhanced';

if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
}
if (!fs.existsSync(path.join(targetDir, 'css'))) {
    fs.mkdirSync(path.join(targetDir, 'css'));
}
if (!fs.existsSync(path.join(targetDir, 'js'))) {
    fs.mkdirSync(path.join(targetDir, 'js'));
}

const html = fs.readFileSync(srcPath, 'utf8');

// Extract CSS
const styleMatch = html.match(/<style>([\s\S]*?)<\/style>/);
let css = styleMatch ? styleMatch[1] : '';

// Extract JS
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
let js = scriptMatch ? scriptMatch[1] : '';

// Replace in HTML
let newHtml = html.replace(/<style>[\s\S]*?<\/style>/, '<link rel="stylesheet" href="css/styles.css">');
newHtml = newHtml.replace(/<script>[\s\S]*?<\/script>/, '<script src="js/main.js"></script>');

fs.writeFileSync(path.join(targetDir, 'index.html'), newHtml);
fs.writeFileSync(path.join(targetDir, 'css', 'styles.css'), css);
fs.writeFileSync(path.join(targetDir, 'js', 'main.js'), js);

console.log('Split completed successfully.');
