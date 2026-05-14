import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text=f.read()

tables = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', text)
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_rows_sample.txt','w',encoding='utf-8') as out:
    for i, row in enumerate(tables[:30]):
        out.write(f'--- Row {i} ---\n')
        out.write(row[:500] + '\n')
