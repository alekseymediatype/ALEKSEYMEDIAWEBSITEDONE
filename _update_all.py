import re, glob, os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-14', content)
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-14', content)
    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No change', os.path.basename(path))
