import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_raw.html','r',encoding='utf-8') as f:
    text=f.read()
scripts=re.findall(r'<script[^>]*>([\s\S]*?)</script>', text)
matches=[]
for s in scripts:
    for m in re.finditer(r'\{[^}]*"name"[^}]*\}', s):
        matches.append(m.group())
    for m in re.finditer(r'\{[^}]*"address"[^}]*\}', s):
        matches.append(m.group())
print('Found', len(matches), 'potential JSON objects')
for m in matches[:20]:
    print(m)
