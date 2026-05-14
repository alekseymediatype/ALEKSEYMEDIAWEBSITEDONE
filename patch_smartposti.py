import sys
sys.stdout.reconfigure(encoding='utf-8')

import json

with open('smartposti_parsed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix the bad name
for r in data:
    if r['url'] == 'https://www.smartposti.lv/atrasanas-vietas/smartposti-pakomats-top-m-nometnu':
        r['name'] = 'Smartposti top! M. Nometņu'
        print(f"Fixed: {r['name']}")

# Add missing entries
data.append({
    'carrier': 'SMARTPOSTI',
    'name': 'Smartposti māja Vaidavas',
    'city': 'Rīga',
    'postal': 'LV-1084',
    'address': 'Vaidavas iela 1C',
    'url': 'https://www.smartposti.lv/atrasanas-vietas/smartposti-maja-vaidavas'
})
print("Added: Smartposti māja Vaidavas")

data.append({
    'carrier': 'SMARTPOSTI',
    'name': 'Smartposti Mego Rīgas Baloži',
    'city': 'Baloži',
    'postal': 'LV-2112',
    'address': 'Rīgas iela 14',
    'url': 'https://www.smartposti.lv/atrasanas-vietas/smartposti-pakomats-mego-rigas-balozi'
})
print("Added: Smartposti Mego Rīgas Baloži")

print(f"\nTotal entries: {len(data)}")

# Save updated JSON
with open('smartposti_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Generate JS lines
js_lines = []
for r in data:
    js_lines.append(f'  {{ carrier: "{r["carrier"]}", name: "{r["name"]}", city: "{r["city"]}", postal: "{r["postal"]}", address: "{r["address"]}" }},')

with open('smartposti_js_array.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(js_lines))

print(f"Wrote {len(js_lines)} JS lines")
