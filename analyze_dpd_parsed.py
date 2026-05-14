import json
from collections import Counter

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_parsed.json','r',encoding='utf-8') as f:
    data = json.load(f)

cities = Counter(r['city'] for r in data)
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_analysis2.txt','w',encoding='utf-8') as out:
    out.write(f'Total DPD points: {len(data)}\n')
    out.write(f'Cities count: {len(cities)}\n')
    out.write('\nTop cities:\n')
    for city, count in cities.most_common(50):
        out.write(f'  {city}: {count}\n')
