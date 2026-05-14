import json, sys
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_map_data.json','r',encoding='utf-8') as f:
    data = json.load(f)
print(type(data))
if isinstance(data, list):
    print('List length:', len(data))
    if len(data) > 0:
        print('First item keys:', list(data[0].keys()) if isinstance(data[0], dict) else 'not dict')
        print('First item:', json.dumps(data[0], ensure_ascii=False, indent=2)[:1000])
elif isinstance(data, dict):
    print('Dict keys:', list(data.keys())[:20])
    for k, v in data.items():
        print(k, type(v), len(v) if hasattr(v, '__len__') else '')
        if isinstance(v, list) and len(v) > 0:
            print('First item keys:', list(v[0].keys()) if isinstance(v[0], dict) else 'not dict')
            print('First item:', json.dumps(v[0], ensure_ascii=False, indent=2)[:1000])
            break
        break
