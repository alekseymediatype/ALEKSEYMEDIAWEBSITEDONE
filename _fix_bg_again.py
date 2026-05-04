import glob, re, os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for fname in glob.glob(os.path.join(BASE, '*.html')):
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    # Remove existing background-color from inline style blocks
    content = re.sub(
        r'\u003cstyle\u003e\s*html,\s*body\s*\{\s*color:\s*#f4eadb;(?:\s*background-color:\s*#[^;]+;)?\s*\}',
        r'\u003cstyle\u003e\n    html, body { color: #f4eadb; }',
        content,
    )
    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(fname))
    else:
        print('No change', os.path.basename(fname))
