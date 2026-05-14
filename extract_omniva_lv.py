import json, re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_map_data.json','r',encoding='utf-8') as f:
    data = json.load(f)

machines = data.get('parcel_machines', [])
lv = [m for m in machines if m.get('country_id') == 'LV']

out_lines = []
for m in lv:
    zipcode = m.get('ZIP','')
    title = m.get('title','')
    address = m.get('address_text','')
    desc = m.get('description','')
    # Try to extract city from description or address
    # Format: { carrier: "OMNIVA", name: "... pakomāts", city: "...", postal: "LV-...", address: "..." }
    out_lines.append({
        'zip': zipcode,
        'title': title,
        'address': address,
        'desc': desc
    })

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_lv_raw.json','w',encoding='utf-8') as f:
    json.dump(out_lines, f, ensure_ascii=False, indent=2)

print('Extracted', len(lv), 'LV machines')
