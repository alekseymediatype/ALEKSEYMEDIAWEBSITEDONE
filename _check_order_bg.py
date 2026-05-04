import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Find rules that contain .order-page-view, .order-delivery-view, .order-payment-view and background
keywords = ['order-page-view', 'order-delivery-view', 'order-payment-view']
color_patterns = ['78,103,146', '142,166,207', '104,130,170', '15,31,58', '42,171,238']

# Split by }
blocks = re.split(r'\}\s*\n(?=\.)', content)

for block in blocks:
    block = block.strip()
    if not block:
        continue
    # Check if block starts with a relevant selector
    first_part = block.split('{')[0].strip() if '{' in block else block[:200]
    if any(k in first_part for k in keywords):
        # Check if it contains background or blue colors
        if 'background' in block.lower() or any(c in block for c in color_patterns):
            print('---')
            print(first_part[:200])
            # Print only the background-containing lines
            for line in block.splitlines():
                if 'background' in line.lower() or 'color' in line.lower() or 'box-shadow' in line:
                    print('  ', line.strip()[:200])
            print()
