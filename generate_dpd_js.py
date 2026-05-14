import json

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_parsed.json','r',encoding='utf-8') as f:
    data = json.load(f)

lines = []
for r in data:
    name = r['name'].replace('Paku Skapis ', 'DPD ')
    city = r['city']
    postal = r['postal']
    address = r['address']
    lines.append(f'  {{ carrier: "DPD", name: "{name}", city: "{city}", postal: "{postal}", address: "{address}" }},')

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_js_array.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Generated {len(lines)} DPD JS lines')
