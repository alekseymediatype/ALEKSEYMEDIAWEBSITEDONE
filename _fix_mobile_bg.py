import re
import glob
import os

BASE = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3'

# 1) Fix the mobile media query in CSS to use the SAME warm gradient as desktop
with open(os.path.join(BASE, 'styles.css'), 'r', encoding='utf-8') as f:
    css = f.read()

old_mobile_bg = """@media (max-width: 980px) {
  body, html{
    background: radial-gradient(ellipse at 50% 0%, #121520 0%, #0a0c14 50%, #06070a 100%) !important;
  }
  .topbar { backdrop-filter: none !important; -webkit-backdrop-filter: none !important; background:#0a0c14 !important; }"""

new_mobile_bg = """@media (max-width: 980px) {
  body, html{
    background: radial-gradient(ellipse at 50% 0%, #1a1714 0%, #120f0c 50%, #0d0b09 100%) !important;
  }
  .topbar { backdrop-filter: none !important; -webkit-backdrop-filter: none !important; background:#120f0c !important; }"""

css = css.replace(old_mobile_bg, new_mobile_bg)

with open(os.path.join(BASE, 'styles.css'), 'w', encoding='utf-8') as f:
    f.write(css)
print('Fixed mobile background in styles.css')

# 2) Remove inline background-color from ALL HTML files so body gradient applies everywhere
for path in glob.glob(os.path.join(BASE, '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    old = content
    # Remove background-color from inline style blocks (all variants)
    content = re.sub(
        r'html,\s*body\s*\{\s*color:\s*#f4eadb;\s*background-color:\s*#[^;]+;\s*\}',
        'html, body { color: #f4eadb; }',
        content
    )
    # Also bump versions
    content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-11', content)
    content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-11', content)
    if content != old:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', os.path.basename(path))
    else:
        print('No change', os.path.basename(path))

print('Done.')
