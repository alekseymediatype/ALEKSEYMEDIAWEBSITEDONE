import re
from collections import Counter

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_analysis.txt','w',encoding='utf-8') as out:
    panels = re.findall(r'<div[^>]*class="[^"]*dpd-table[^"]*"[^>]*>([\s\S]*?)</div>', text)
    out.write(f'Found {len(panels)} dpd-table containers\n')

    all_divs = re.findall(r'<div[^>]*>', text)
    out.write(f'Total div tags: {len(all_divs)}\n')

    streets = ['iela', 'prospekts', 'laukums', 'ceļš', 'gatve', 'bulvāris', 'šoseja']
    found = []
    for s in streets:
        c = text.count(s)
        if c > 0:
            found.append((s, c))
    out.write('Street keyword counts: ' + str(found) + '\n')

    postals = re.findall(r'LV-\d{4}', text)
    out.write(f'Found {len(postals)} LV postal codes\n')
    if postals:
        out.write('Samples: ' + str(postals[:20]) + '\n')
