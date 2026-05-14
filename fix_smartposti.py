import sys
sys.stdout.reconfigure(encoding='utf-8')

import json
import urllib.request
import re

with open('smartposti_parsed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find entries with suspicious names
suspicious = []
for r in data:
    name = r['name']
    if len(name) < 15 or name.endswith(' M') or name.endswith(' k') or '.' in name.replace('Smartposti ', ''):
        suspicious.append(r)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

for r in suspicious:
    url = r['url']
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode('utf-8')
        m = re.search(r'<meta name="description" content="([^"]+)"', html)
        if m:
            desc = m.group(1)
            print(f"URL: {url}")
            print(f"Current name: {r['name']}")
            print(f"Description: {desc}")
            print()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
