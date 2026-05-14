import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\omniva_baltic_js_array.txt', 'r', encoding='utf-8') as f:
    new_block = f.read()

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js', 'r', encoding='utf-8') as f:
    script = f.read()

# Find old block boundaries
start_marker = '/* Omniva */'
end_marker = '/* DPD */'

start_idx = script.find(start_marker)
end_idx = script.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: markers not found. start={start_idx}, end={end_idx}")
    exit(1)

old_block = script[start_idx:end_idx]

# Replace
script = script.replace(old_block, new_block + '\n', 1)

with open(r'C:\Users\Aleksey Ilnickiy\Desktop\AM\script.js', 'w', encoding='utf-8') as f:
    f.write(script)

print("Successfully replaced Omniva block with Baltic data")
print(f"Old block length: {len(old_block)} chars")
print(f"New block length: {len(new_block)} chars")
print(f"New script.js size: {len(script)} chars")
