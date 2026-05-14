import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

panels = re.findall(r'<div[^>]*class="[^"]*dpd-table[^"]*"[^>]*>([\s\S]*?)</div>', text)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_table_samples.txt','w',encoding='utf-8') as out:
    out.write(f'Total panels: {len(panels)}\n')
    for i, panel in enumerate(panels[:20]):
        out.write(f'\n--- Panel {i} ---\n')
        # Extract first few text nodes
        texts = re.findall(r'<p>([^<]*)</p>', panel)
        out.write(str(texts[:10]) + '\n')
