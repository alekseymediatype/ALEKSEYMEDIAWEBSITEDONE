import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all body selector blocks in the CSS
# body.whatever {
#   ...
# }
multi_blocks = re.findall(r'(body\.\w[^{]*\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})', content, re.DOTALL)
single_blocks = re.findall(r'(body\.\w[^{]*\{[^{}]*\})', content, re.DOTALL)

all_blocks = list(set(multi_blocks + single_blocks))

for block in sorted(all_blocks, key=lambda x: content.index(x)):
    print('---')
    print(block[:400])
    print()
