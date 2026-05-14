import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js','r',encoding='utf-8') as f:
    text = f.read()

start = text.find('const parcelLockers = [')
end = text.find('];', start)
array_text = text[start:end]

riga_omniva = len(re.findall(r'carrier: "OMNIVA".*city: "Rīga"', array_text))
riga_dpd = len(re.findall(r'carrier: "DPD".*city: "Rīga"', array_text))

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\riga_count.txt','w',encoding='utf-8') as out:
    out.write(f'OMNIVA Riga: {riga_omniva}\n')
    out.write(f'DPD Riga: {riga_dpd}\n')
