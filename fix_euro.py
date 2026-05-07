# -*- coding: utf-8 -*-
with open(r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3\script.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Build euro from UTF-8 bytes to avoid symbol filtering
euro = b'\xe2\x82\xac'.decode('utf-8')
lines[4211] = "  return `${Number(amount).toFixed(2).replace('.', ',')} " + euro + "`;\n"

with open(r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3\script.js', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Fixed euro using byte decode')
