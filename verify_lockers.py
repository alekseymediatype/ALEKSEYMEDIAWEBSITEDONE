import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','r',encoding='utf-8') as f:
    text = f.read()

start = text.find('const parcelLockers = [')
end = text.find('];', start)
array_text = text[start:end]

omniva = array_text.count('carrier: "OMNIVA"')
dpd = array_text.count('carrier: "DPD"')

print(f'OMNIVA: {omniva}')
print(f'DPD: {dpd}')
print(f'Total: {omniva + dpd}')

# Check for any lines that don't end with comma (except the last one)
lines = [l for l in array_text.split('\n') if l.strip().startswith('{ carrier:')]
bad_lines = []
for i, line in enumerate(lines):
    stripped = line.rstrip()
    if not stripped.endswith(','):
        # The very last line before ]; should not end with comma
        if i < len(lines) - 1:
            bad_lines.append((i+1, stripped[:80]))

print(f'Lines missing comma: {len(bad_lines)}')
for num, content in bad_lines:
    print(f'  Line {num}: {content}')
