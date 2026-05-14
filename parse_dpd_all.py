import re

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_raw.html','r',encoding='utf-8') as f:
    text = f.read()

sections = []
pattern = re.compile(r'<h3[^>]*>([<>\s\S]*?)</h3>[\s\S]*?<div class="collapsible-content[^"]*"[^>]*>([\s\S]*?)</div>')
for m in pattern.finditer(text):
    h3_text = re.sub(r'<[^>]*>', '', m.group(1)).strip()
    content = m.group(2)
    sections.append((h3_text, content))

results = []
# Mapping for special sections
section_city_map = {
    'Izņemšanas laiki darba dienās': 'Rīga',
}

for section_title, content in sections:
    # Determine base city from section title
    base_city = section_city_map.get(section_title, '')
    if not base_city and section_title not in ['Adrese', 'Paku Skapju meklētājs Latvijā', '']:
        base_city = section_title

    rows = re.findall(r'<tr[^>]*>([\s\S]*?)</tr>', content)
    for row in rows:
        cells = re.findall(r'<td[^>]*>([\s\S]*?)</td>', row)
        if len(cells) < 2:
            continue
        name = re.sub(r'<[^>]*>', '', cells[0]).strip()
        address_line = re.sub(r'<[^>]*>', '', cells[1]).strip()

        if not name or not address_line:
            continue
        if 'Paku Skapis' not in name and 'iela' not in address_line and 'gatve' not in address_line and 'prospekts' not in address_line:
            continue

        # Extract postal code
        postal_match = re.search(r'(LV-\d{4})', address_line)
        postal = postal_match.group(1) if postal_match else ''
        address = re.sub(r',?\s*LV-\d{4}', '', address_line).strip()
        # Remove trailing comma
        address = re.sub(r',\s*$', '', address).strip()

        # Determine city
        city = base_city
        if not city:
            # Try to extract from name like "Paku Skapis VIRŠI Aglona"
            # Remove "Paku Skapis" prefix
            cleaned = re.sub(r'^Paku Skapis\s+', '', name)
            # Look for known city patterns in remaining text
            # Heuristic: if remaining text starts with a known word that looks like a city
            # We'll use a simple approach: if name contains city after first word
            parts = cleaned.split()
            if len(parts) >= 2:
                # Try last word or second word as city
                # But it's risky, better to rely on base_city for most cases
                pass

        if city:
            results.append({
                'name': name,
                'city': city,
                'postal': postal,
                'address': address
            })

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_parsed.json','w',encoding='utf-8') as f:
    import json
    json.dump(results, f, ensure_ascii=False, indent=2)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\dpd_parsed_log.txt','w',encoding='utf-8') as f:
    f.write(f'Total parsed: {len(results)}\n')
    for r in results[:50]:
        f.write(f"{r['city']} | {r['name']} | {r['address']} | {r['postal']}\n")
