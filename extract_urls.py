import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_js.js','r',encoding='utf-8') as f:
    text=f.read()
# Extract strings that look like API paths
matches = re.findall(r'"(/[^"]*(?:api|json|locations|pakomati|terminals|machines|points)[^"]*)"', text)
matches += re.findall(r"'(/[^']*(?:api|json|locations|pakomati|terminals|machines|points)[^']*)'", text)
# Also full URLs
matches += re.findall(r'"https?://[^"]*(?:api|json|locations|pakomati|terminals|machines|points)[^"]*"', text)
matches += re.findall(r"'https?://[^']*(?:api|json|locations|pakomati|terminals|machines|points)[^']*'", text)
seen=set()
for m in matches:
    if m not in seen:
        seen.add(m)
        print(m)
print(f"\nTotal unique matches: {len(seen)}")
