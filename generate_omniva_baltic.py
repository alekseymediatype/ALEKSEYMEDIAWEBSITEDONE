import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_map_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

machines = data.get('parcel_machines', [])
countries = {'LV': 'Latvija', 'LT': 'Lietuva', 'EE': 'Igaunija'}

js_lines = []
for country_code in ['LV', 'LT', 'EE']:
    country_machines = [m for m in machines if m.get('country_id') == country_code]
    if not country_machines:
        continue
    js_lines.append(f'/* Omniva {countries[country_code]} */')
    for m in country_machines:
        zipcode = m.get('ZIP', '')
        title = m.get('title', '').strip()
        address_text = m.get('address_text', '').strip()

        postal = f"LV-{zipcode}" if country_code == 'LV' and zipcode else zipcode
        parts = [p.strip() for p in address_text.split(',')]
        if parts and re.match(r'^\d{4}$', parts[-1]):
            parts = parts[:-1]

        city = ''
        street = ''
        if len(parts) >= 2:
            city = parts[-1]
            if any(x in city.lower() for x in ['pagasts', 'novads', 'ciems', 'vald']):
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

        js_lines.append(f'  {{ carrier: "OMNIVA", name: "{name}", city: "{city}", postal: "{postal}", address: "{street}" }},')

output_path = r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_baltic_js_array.txt'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(js_lines))

print(f'Generated {len(js_lines)} lines for Omniva Baltic')
print(f'Countries: LV={len([m for m in machines if m.get("country_id")=="LV"])}, LT={len([m for m in machines if m.get("country_id")=="LT"])}, EE={len([m for m in machines if m.get("country_id")=="EE"])}')
