import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','r',encoding='utf-8') as f:
    text = f.read()

# Find parcelLockers array
start = text.find('const parcelLockers = [')
end = text.find('];', start) + 2
array_text = text[start:end]

omniva = array_text.count('carrier: "OMNIVA"')
dpd = array_text.count('carrier: "DPD"')
smartposti = array_text.count('carrier: "SMARTPOSTI"')

print(f'OMNIVA: {omniva}')
print(f'DPD: {dpd}')
print(f'SMARTPOSTI: {smartposti}')
print(f'Total JS file size: {len(text)} chars')
