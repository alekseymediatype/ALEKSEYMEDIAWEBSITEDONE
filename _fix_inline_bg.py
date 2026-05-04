import re, glob, os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    old = content

    # Replace inline style blocks: add the gradient background directly
    # Pattern 1: simple <style>html, body { color: #f4eadb; }\n    body { margin: 0; }</style>
    content = re.sub(
        r'\u003cstyle\u003e\s*html,\s*body\s*\{\s*color:\s*#f4eadb;\s*\}\s*body\s*\{\s*margin:\s*0;\s*\}\s*\u003c/style\u003e',
        r'\u003cstyle\u003e\n    html, body { color: #f4eadb; background: radial-gradient(ellipse at 50% 0%, #1a1714 0%, #120f0c 50%, #0d0b09 100%); }\n    body { margin: 0; }\n  \u003c/style\u003e',
        content
    )

    # Pattern 2: with topbar/nav extras
    content = re.sub(
        r'\u003cstyle\u003e\s*html,\s*body\s*\{\s*color:\s*#f4eadb;\s*\}\s*body\s*\{\s*margin:\s*0;\s*\}\s*\.topbar\s*\{[^}]*\}\s*\.nav\s*\{[^}]*\}\s*\u003c/style\u003e',
        r'\u003cstyle\u003e\n    html, body { color: #f4eadb; background: radial-gradient(ellipse at 50% 0%, #1a1714 0%, #120f0c 50%, #0d0b09 100%); }\n    body { margin: 0; }\n    .topbar { position: fixed; top: 0; left: 0; width: 100%; z-index: 1000; }\n    .nav { min-height: 88px; }\n  \u003c/style\u003e',
        content
    )

    # Bump versions
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-12', content)
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-12', content)

    if content != old:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No change', os.path.basename(path))
