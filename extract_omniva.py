import json

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_map_data.json','r',encoding='utf-8') as f:
    data = json.load(f)

machines = data.get('parcel_machines', [])
print('Total machines:', len(machines))

# Check country IDs
from collections import Counter
countries = Counter(m['country_id'] for m in machines)
print('Country IDs:', countries.most_common())

# Show first 5 LV machines (assuming LV is country_id 2 or something)
for m in machines[:10]:
    print(m['country_id'], m['ZIP'], m['title'], m.get('address_text',''))
