import re
path = r'C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3\merch.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()
content = re.sub(r'styles\.css\?v=[^"\'\s>]+', 'styles.css?v=20260503-02', content)
content = re.sub(r'script\.js\?v=[^"\'\s>]+', 'script.js?v=20260503-02', content)
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('merch.html updated to v=20260503-02')
