import re, glob, os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    old = content

    # Find the inline style block and replace it
    # Pattern finds: <style> html, body { color: #f4eadb; } body { margin: 0; } ... optional .topbar/.nav ... </style>
    # We replace the whole block with a new one that includes the background gradient

    # Simple replacement: just replace body { margin: 0; } with body { margin: 0; background: ... }
    content = re.sub(
        r'body\s*\{\s*margin:\s*0;\s*\}',
        r'body { margin: 0; background: radial-gradient(ellipse at 50% 0%, #1a1714 0%, #120f0c 50%, #0d0b09 100%); }',
        content,
    )

    # Also bump versions
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-12', content)
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-12', content)

    if content != old:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No change', os.path.basename(path))
