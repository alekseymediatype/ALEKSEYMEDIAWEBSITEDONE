import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','r',encoding='utf-8') as f:
    js_text = f.read()

# Find parcelLockers array bounds
start_marker = 'const parcelLockers = ['
start_idx = js_text.find(start_marker)
if start_idx == -1:
    print('ERROR: parcelLockers not found')
    exit(1)

array_start = start_idx + len(start_marker)
end_idx = js_text.find('];', array_start)
if end_idx == -1:
    print('ERROR: closing ]; not found')
    exit(1)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_js_array.txt','r',encoding='utf-8') as f:
    omniva_lines = f.read().strip().split('\n')

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_js_array.txt','r',encoding='utf-8') as f:
    dpd_lines = f.read().strip().split('\n')

new_array_lines = []
new_array_lines.append('/* Omniva */')
for line in omniva_lines:
    new_array_lines.append(line)
new_array_lines.append('')
new_array_lines.append('/* DPD */')
for line in dpd_lines:
    new_array_lines.append(line)

new_array_text = '\n'.join(new_array_lines)

new_js = js_text[:start_idx + len(start_marker)] + '\n' + new_array_text + '\n' + js_text[end_idx:]

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','w',encoding='utf-8') as f:
    f.write(new_js)

print(f'Updated: {len(omniva_lines)} Omniva + {len(dpd_lines)} DPD = {len(omniva_lines)+len(dpd_lines)} total')
