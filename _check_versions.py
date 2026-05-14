
\import re, glob, os

BASE = r"C:\Users\Aleksey Ilnickiy\Music\готовый сайт 3"

def get_new_version(old):
    # extract date part and bump revision
    m = re.match(r'(\d{8})-(\d{2})$', old)
    if m:
        date, rev = m.groups()
        new_rev = str(int(rev) + 1).zfill(2)
        return f"{date}-{new_rev}"
    return "20260503-01"

for path in glob.glob(os.path.join(BASE, "*.html")):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    versions = set(re.findall(r'\?v=([^"\'\\]+)', content))
    print(os.path.basename(path), versions)
