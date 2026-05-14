import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text=f.read()

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_search_result.txt','w',encoding='utf-8') as out:
    out.write('Riga count: ' + str(text.count('Riga')) + '\n')
    out.write('Daugavpils count: ' + str(text.count('Daugavpils')) + '\n')
    out.write('File length: ' + str(len(text)) + '\n')

    # Find table rows
    tables = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', text)
    out.write('Table rows found: ' + str(len(tables)) + '\n')

    # Show first few rows containing Riga
    for row in tables[:50]:
        if 'Riga' in row or 'Rīga' in row:
            out.write('---\n')
            out.write(row[:800] + '\n')
