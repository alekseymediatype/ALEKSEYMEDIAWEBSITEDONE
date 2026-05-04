import re
with open('merch.html', 'r', encoding='utf-8') as f:
    content = f.read()
for m in re.finditer(r'styles\.css.*?v=([^\'\"\\s]+)', content):
    print('merch styles version:', m.group(1))
