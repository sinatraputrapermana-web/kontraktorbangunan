import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

classes = set()
for m in re.finditer(r'class=["\']([^"\']+)["\']', content):
    for c in m.group(1).split():
        classes.add(c)

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

missing_in_style = []
for c in sorted(classes):
    pattern = r'(\.' + re.escape(c) + r'[\s,\.:\{>+~\[])'
    if not re.search(pattern, style_css):
        missing_in_style.append(c)

print('Classes in index.html NOT in style.css:')
print(missing_in_style)
