import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import re

with open('smartposti_parsed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find potentially bad names
for r in data:
    name = r['name']
    if len(name) < 15 or name.endswith(' M') or name.endswith(' k') or '.' in name.replace('Smartposti ', ''):
        print(f"{name} | {r['address']} | {r['city']}")
