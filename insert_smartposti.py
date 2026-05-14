import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\smartposti_js_array.txt', 'r', encoding='utf-8') as f:
    smartposti_lines = f.read()

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js', 'r', encoding='utf-8') as f:
    script = f.read()

old_str = '  { carrier: "DPD", name: "DPD Elvi Zvejniekciems", city: "Zvejniekciems", postal: "LV-2160", address: "Ainažu iela 113" },\n];'

new_str = '  { carrier: "DPD", name: "DPD Elvi Zvejniekciems", city: "Zvejniekciems", postal: "LV-2160", address: "Ainažu iela 113" },\n\n/* Smartposti */\n' + smartposti_lines + '\n];'

if old_str not in script:
    print("ERROR: old_str not found in script.js")
    # Try to find the close
    idx = script.find('DPD Elvi Zvejniekciems')
    if idx != -1:
        print(f"Found at index {idx}")
        print(repr(script[idx-5:idx+200]))
else:
    script = script.replace(old_str, new_str, 1)
    with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js', 'w', encoding='utf-8') as f:
        f.write(script)
    print("Successfully inserted Smartposti packomats into script.js")
