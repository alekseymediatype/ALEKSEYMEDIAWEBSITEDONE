import sys
sys.stdout.reconfigure(encoding='utf-8')

import urllib.request
import xml.etree.ElementTree as ET
import re
import json
import time
import concurrent.futures

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch(url):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        try:
            print(f"Error fetching {url}: {e}")
        except:
            pass
        return None

def parse_location(html, url):
    if not html:
        return None
    m = re.search(r'<meta name="description" content="([^"]+)"', html)
    if not m:
        try:
            print(f"No description found for {url}")
        except:
            pass
        return None
    desc = m.group(1).strip()

    prefixes = ['SmartPosti pakomāts ', 'SmartPosti kiosks ']
    matched_prefix = None
    for prefix in prefixes:
        if desc.startswith(prefix):
            matched_prefix = prefix
            break

    if not matched_prefix:
        try:
            print(f"Unexpected prefix in {url}: {desc[:50]}")
        except:
            pass
        return None

    rest = desc[len(matched_prefix):]

    # Try to match: Name. Street, Postal City. Description...
    # Some addresses have "1905. gada iela" which contains a dot, so we need to be careful
    # Pattern: capture everything up to the first ". " that is followed by an address
    # The address format is: {street}, {postal} {city}.
    # Let's match greedily for the name, then look for ", XXXX City."
    match = re.match(r'^(.+?)\.\s+(.+?),\s+(\d{4})\s+(.+?)\.\s+SmartPosti', rest)
    if not match:
        match = re.match(r'^(.+?)\.\s+(.+?),\s+(\d{4})\s+(.+?)\.\s*', rest)

    if not match:
        try:
            print(f"Could not parse description for {url}: {rest[:100]}")
        except:
            pass
        return None

    name = match.group(1).strip()
    address = match.group(2).strip()
    postal = f"LV-{match.group(3)}"
    city = match.group(4).strip()

    # Clean up name - remove prefix artifacts
    for prefix in prefixes:
        name = name.replace(prefix, '')

    return {
        'carrier': 'SMARTPOSTI',
        'name': f'Smartposti {name}',
        'city': city,
        'postal': postal,
        'address': address,
        'url': url
    }

def process_url(url):
    html = fetch(url)
    result = parse_location(html, url)
    if result:
        return result
    return None

def main():
    sitemap_url = 'https://www.smartposti.lv/sitemap-locations.xml'
    try:
        print("Fetching sitemap...")
    except:
        pass
    sitemap_xml = fetch(sitemap_url)
    if not sitemap_xml:
        print("Failed to fetch sitemap")
        return

    root = ET.fromstring(sitemap_xml)
    urls = []
    for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        urls.append(url_elem.text.strip())

    try:
        print(f"Found {len(urls)} locations")
    except:
        pass

    results = []
    errors = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_to_url = {executor.submit(process_url, url): url for url in urls}
        for i, future in enumerate(concurrent.futures.as_completed(future_to_url)):
            url = future_to_url[future]
            try:
                result = future.result()
                if result:
                    results.append(result)
                else:
                    errors.append(url)
            except Exception as e:
                try:
                    print(f"Exception for {url}: {e}")
                except:
                    pass
                errors.append(url)

            if (i + 1) % 50 == 0:
                try:
                    print(f"Processed {i + 1}/{len(urls)}...")
                except:
                    pass

    try:
        print(f"\nFirst pass: {len(results)} parsed, {len(errors)} errors")
    except:
        pass

    if errors:
        try:
            print("\nRetrying errors...")
        except:
            pass
        new_errors = []
        for url in errors:
            time.sleep(1)
            try:
                result = process_url(url)
                if result:
                    results.append(result)
                else:
                    new_errors.append(url)
            except Exception as e:
                try:
                    print(f"Retry failed for {url}: {e}")
                except:
                    pass
                new_errors.append(url)
        errors = new_errors
        try:
            print(f"After retry: {len(results)} parsed, {len(errors)} errors")
        except:
            pass

    # Save intermediate results even if some errors remain
    js_lines = []
    for r in results:
        js_lines.append(f'  {{ carrier: "{r["carrier"]}", name: "{r["name"]}", city: "{r["city"]}", postal: "{r["postal"]}", address: "{r["address"]}" }},')

    output_path = r'C:\Users\Aleksey Ilnickiy\Desktop\AM\smartposti_js_array.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(js_lines))

    try:
        print(f"\nWrote {len(js_lines)} lines to {output_path}")
    except:
        pass

    json_path = r'C:\Users\Aleksey Ilnickiy\Desktop\AM\smartposti_parsed.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    try:
        print(f"Wrote JSON to {json_path}")
    except:
        pass

    if errors:
        error_path = r'C:\Users\Aleksey Ilnickiy\Desktop\AM\smartposti_errors.txt'
        with open(error_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(errors))
        try:
            print(f"Wrote {len(errors)} error URLs to {error_path}")
        except:
            pass

if __name__ == '__main__':
    main()
