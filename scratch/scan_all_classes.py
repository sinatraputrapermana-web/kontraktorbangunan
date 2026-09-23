import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html') + glob.glob('layanan/*.html')

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

all_classes = set()
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
        for m in re.finditer(r'class=["\']([^"\']+)["\']', content):
            for c in m.group(1).split():
                all_classes.add(c)

missing = []
for c in sorted(all_classes):
    pattern = r'(\.' + re.escape(c) + r'[\s,\.:\{>+~\[])'
    if not re.search(pattern, style_css):
        missing.append(c)

print(f"Total unique classes in all 80 HTML files: {len(all_classes)}")
print("Missing in style.css:")
for c in missing:
    print(" -", c)
