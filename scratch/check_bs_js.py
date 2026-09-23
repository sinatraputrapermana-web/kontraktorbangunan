import glob
import re

html_files = glob.glob('*.html') + glob.glob('blog/*.html') + glob.glob('layanan/*.html')

bootstrap_js_usages = []
for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        content = f.read()
        if 'data-bs-' in content or 'modal' in content.lower():
            bootstrap_js_usages.append(hf)

print("Files with modal / data-bs- attributes:", bootstrap_js_usages)
