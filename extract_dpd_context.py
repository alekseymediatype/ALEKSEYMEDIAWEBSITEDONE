import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

# Find the divs with dpd-table class
matches = list(re.finditer(r'<div[^>]*class="[^"]*dpd-table[^"]*"[^>]*>', text))

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_context.txt','w',encoding='utf-8') as out:
    for i, m in enumerate(matches[:30]):
        start = max(0, m.start() - 300)
        end = min(len(text), m.end() + 500)
        out.write(f'\n--- Panel {i} context ---\n')
        out.write(text[start:end] + '\n')
