import re, json

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

# Extract all JSON-like structures from script tags
scripts = re.findall(r'<script[^>]*>([\s\S]*?)</script>', text)

matches = []
for s in scripts:
    # Look for arrays of objects
    for m in re.finditer(r'\[[\s\S]{50,5000}?\]', s):
        snippet = m.group()
        if '"address"' in snippet or '"name"' in snippet or '"city"' in snippet or '"title"' in snippet:
            matches.append(snippet[:500])

    # Look for objects with address
    for m in re.finditer(r'\{[\s\S]{30,2000}?\}', s):
        snippet = m.group()
        if '"address"' in snippet or '"name"' in snippet or '"city"' in snippet:
            matches.append(snippet[:500])

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_json_candidates.txt','w',encoding='utf-8') as out:
    out.write(f'Found {len(matches)} candidates\n')
    for i, m in enumerate(matches[:50]):
        out.write(f'--- {i} ---\n')
        out.write(m + '\n')
