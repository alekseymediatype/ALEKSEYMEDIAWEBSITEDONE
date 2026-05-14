import re

# Read current script.js
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','r',encoding='utf-8') as f:
    js_text = f.read()

# Find parcelLockers array bounds
start_marker = 'const parcelLockers = ['
start_idx = js_text.find(start_marker)
if start_idx == -1:
    print('ERROR: parcelLockers not found')
    exit(1)

# Find the matching closing bracket
# Since the array is large, we need to find the exact `];` that closes it
# The array starts after `const parcelLockers = [`
array_start = start_idx + len(start_marker)
# Find the next `];` after array_start
end_idx = js_text.find('];', array_start)
if end_idx == -1:
    print('ERROR: closing ]; not found')
    exit(1)

array_text = js_text[array_start:end_idx]

# Extract DPD entries
lines = array_text.split('\n')
dpd_lines = [line for line in lines if 'carrier: "DPD"' in line]
print(f'Found {len(dpd_lines)} DPD entries to keep')

# Read new Omniva entries
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_js_array.txt','r',encoding='utf-8') as f:
    omniva_lines = f.read().strip().split('\n')
print(f'Read {len(omniva_lines)} new Omniva entries')

# Build new array text
# DPD lines might have trailing commas issues; ensure they end with commas
fixed_dpd = []
for line in dpd_lines:
    line = line.rstrip()
    if not line.endswith(','):
        line += ','
    fixed_dpd.append(line)

new_array_lines = []
new_array_lines.append('/* Omniva */')
for line in omniva_lines:
    new_array_lines.append(line)
new_array_lines.append('')
new_array_lines.append('/* DPD */')
for line in fixed_dpd:
    new_array_lines.append(line)

new_array_text = '\n'.join(new_array_lines)

# Replace in js_text
new_js = js_text[:start_idx + len(start_marker)] + '\n' + new_array_text + '\n' + js_text[end_idx:]

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','w',encoding='utf-8') as f:
    f.write(new_js)

print('Updated script.js successfully')
print(f'New total array lines: {len(omniva_lines) + len(fixed_dpd)}')
