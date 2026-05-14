import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

# Find all collapsible content sections and extract h3 before them
sections = []
pattern = re.compile(r'<h3[^>]*>([<>\s\S]*?)</h3>[\s\S]*?<div class="collapsible-content[^"]*"[^>]*>([\s\S]*?)</div>')
for m in pattern.finditer(text):
    h3_text = re.sub(r'<[^>]*>', '', m.group(1)).strip()
    content = m.group(2)
    sections.append((h3_text, content))

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_full_extract.txt','w',encoding='utf-8') as out:
    out.write(f'Found {len(sections)} sections\n')
    for i, (city, content) in enumerate(sections[:40]):
        out.write(f'\n--- Section {i}: {city} ---\n')
        # Extract table rows with Paku Skapis
        rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', content)
        for row in rows[:10]:
            cells = re.findall(r'<td[^>]*>([\s\S]*?)</td>', row)
            line = ' | '.join(re.sub(r'<[^>]*>', '', c).strip() for c in cells)
            if 'Paku Skapis' in line or 'iela' in line or 'gatve' in line or 'prospekts' in line:
                out.write(line + '\n')
