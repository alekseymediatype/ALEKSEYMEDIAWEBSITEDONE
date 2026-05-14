import re
with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_js.js','r',encoding='utf-8') as f:
    text=f.read()
# Find context around omniva-locations-list
idx = text.find('omniva-locations-list')
print('Index:', idx)
if idx != -1:
    print('Context:')
    print(text[max(0,idx-500):idx+500])
