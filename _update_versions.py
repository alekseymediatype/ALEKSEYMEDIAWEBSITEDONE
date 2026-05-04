import re, glob, os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    # Update CSS versions
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-01', content)
    # Update JS versions
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-01', content)
    # Remove inline body background from index.html style tag
    if os.path.basename(path) == 'index.html':
        content = re.sub(r'html, body \{ background: #120f0c; color: #f4eadb; \}', 'html, body { color: #f4eadb; }', content)
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No changes', os.path.basename(path))
