import json, re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_map_data.json','r',encoding='utf-8') as f:
    data = json.load(f)

machines = data.get('parcel_machines', [])
lv = [m for m in machines if m.get('country_id') == 'LV']

js_lines = []
for m in lv:
    zipcode = m.get('ZIP','')
    title = m.get('title','').strip()
    address_text = m.get('address_text','').strip()

    postal = f"LV-{zipcode}" if zipcode else ''
    parts = [p.strip() for p in address_text.split(',')]
    if parts and re.match(r'^\d{4}$', parts[-1]):
        parts = parts[:-1]

    city = ''
    street = ''
    if len(parts) >= 2:
        city = parts[-1]
        if any(x in city.lower() for x in ['pagasts', 'novads', 'ciems']):
            if len(parts) >= 3:
                city = parts[-2]
                street = ', '.join(parts[:-2])
            else:
                street = parts[0]
        else:
            street = ', '.join(parts[:-1])
    elif len(parts) == 1:
        street = parts[0]

    city = city.replace(' pagasts', '').replace(' novads', '').strip()
    name = title

    js_lines.append({
        'carrier': 'OMNIVA',
        'name': name,
        'city': city,
        'postal': postal,
        'address': street
    })

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_lv_parsed.json','w',encoding='utf-8') as f:
    json.dump(js_lines, f, ensure_ascii=False, indent=2)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_parsed_log.txt','w',encoding='utf-8') as f:
    f.write(f'Parsed {len(js_lines)} Omniva machines\n')
    for line in js_lines[:30]:
        f.write(json.dumps(line, ensure_ascii=False) + '\n')
