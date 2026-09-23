import re

with open('assets/js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Minify JS
min_js = re.sub(r'/\*[\s\S]*?\*/', '', js)
min_js = re.sub(r'//.*', '', min_js)
lines = [l.strip() for l in min_js.splitlines() if l.strip()]
min_js = '\n'.join(lines)

with open('assets/js/main.min.js', 'w', encoding='utf-8') as f:
    f.write(min_js)

print("Generated main.min.js:", len(min_js) / 1024, "KB")
