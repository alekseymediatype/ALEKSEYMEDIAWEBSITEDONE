import glob, os, re

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    old = content

    # Simple replacement of the first line in inline style
    content = content.replace(
        'html, body { color: #f4eadb; }',
        'html, body { color: #f4eadb; background: radial-gradient(ellipse at 50% 0%, #1a1714 0%, #120f0c 50%, #0d0b09 100%); }',
    )

    # Also bump versions
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-13', content)
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-13', content)

    if content != old:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No change', os.path.basename(path))
