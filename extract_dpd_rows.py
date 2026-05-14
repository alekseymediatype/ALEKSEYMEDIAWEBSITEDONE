import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

# Extract all table rows
rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', text)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_rows_extracted.txt','w',encoding='utf-8') as out:
    count = 0
    for row in rows:
        # Extract text from td cells
        cells = re.findall(r'<td[^>]*>([\s\S]*?)</td>', row)
        text_content = ' | '.join(re.sub(r'<[^>]*>', '', c).strip() for c in cells)
        # Keep rows with Paku Skapis or street keywords
        if 'Paku Skapis' in text_content or any(k in text_content for k in [' iela ', ' ielas ', 'gatve', 'prospekts', 'laukums', 'bulvāris']):
            if count < 500:
                out.write(text_content + '\n')
            count += 1
    out.write(f'\nTotal matching rows: {count}\n')
