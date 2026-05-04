import re, glob

for path in glob.glob('*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all style links and script src versions
    styles = re.findall(r'styles\.css\?v=([^"\'\s>]+)', content)
    scripts = re.findall(r'script\.js\?v=([^"\'\s>]+)', content)
    # Check for inline backgrounds
    inline_bg = []
    for match in re.finditer(r'<style[^>]*>(.*?)</style>', content, re.DOTALL):
        block = match.group(1)
        if 'background' in block.lower():
            for line in block.splitlines():
                if 'background' in line.lower():
                    inline_bg.append(line.strip())
                    break

    print(os.path.basename(path), 'styles:', styles, 'scripts:', scripts, 'inline_bg_count:' , len(inline_bg))
    for ib in inline_bg:
        print('   inline:', ib[:120])
