import os
import re
import glob

def optimize_html(filepath, is_sub=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '../' if is_sub else ''

    # 1. Optimize preconnect and fonts/css in <head>
    # Find the font and css block
    # Pattern to match font and bootstrap links
    font_cdn_pattern = re.compile(
        r'<link\s+rel=[\"\']preconnect[\"\']\s+href=[\"\']https://fonts\.googleapis\.com[\"\']\s*/?>\s*'
        r'<link\s+rel=[\"\']preconnect[\"\']\s+href=[\"\']https://fonts\.gstatic\.com[\"\']\s+crossorigin\s*/?>\s*'
        r'<link\s+href=[\"\']https://fonts\.googleapis\.com/css2\?family=Plus\+Jakarta\+Sans[^\"\']*[\"\']\s+rel=[\"\']stylesheet[\"\']\s*/?>\s*'
        r'<link\s+href=[\"\']https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.3/dist/css/bootstrap\.min\.css[\"\']\s+rel=[\"\']stylesheet[\"\']\s*/?>\s*'
        r'<link\s+href=[\"\']https://cdn\.jsdelivr\.net/npm/bootstrap-icons@1\.11\.3/font/bootstrap-icons\.css[\"\']\s+rel=[\"\']stylesheet[\"\']\s*/?>',
        re.DOTALL
    )

    hero_preload = f'<link rel="preload" as="image" href="{prefix}assets/img/web/hero.webp" fetchpriority="high" />\n    ' if filepath.endswith('index.html') else ''

    optimized_head_links = (
        f'<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        f'    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        f'    <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />\n'
        f'    {hero_preload}'
        f'<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" />\n'
        f'    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" media="print" onload="this.media=\'all\'" />\n'
        f'    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" /></noscript>\n'
        f'    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" />\n'
        f'    <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" />\n'
        f'    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" media="print" onload="this.media=\'all\'" />\n'
        f'    <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css" /></noscript>'
    )

    new_content, count = font_cdn_pattern.subn(optimized_head_links, content)
    if count == 0:
        # Try looser matching if slightly different formatting
        looser_pattern = re.compile(
            r'<link[^>]*fonts\.googleapis\.com[^>]*>.*?<link[^>]*bootstrap-icons[^>]*>',
            re.DOTALL
        )
        new_content, count = looser_pattern.subn(optimized_head_links, content)

    # 2. Defer bottom scripts
    new_content = re.sub(
        r'<script\s+src=[\"\']https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.3/dist/js/bootstrap\.bundle\.min\.js[\"\'](?!\s+defer)>',
        r'<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer>',
        new_content
    )
    new_content = re.sub(
        r'<script\s+src=[\"\'](\.\./)?assets/js/main\.js[\"\'](?!\s+defer)>',
        lambda m: f'<script src="{m.group(1) or ""}assets/js/main.js" defer>',
        new_content
    )

    # 3. Add width, height, decoding to .brand-mark images
    new_content = re.sub(
        r'<img\s+src=[\"\']([^\"\']*favicon\.jpeg)[\"\']\s+alt=[\"\']Logo[\"\']\s+class=[\"\']brand-mark[\"\'](?![^>]*width)>',
        r'<img src="\1" alt="Logo" class="brand-mark" width="34" height="34" decoding="async">',
        new_content
    )

    # 4. Hero image on index.html
    if filepath.endswith('index.html'):
        hero_pattern = re.compile(
            r'<img\s+src=[\"\']assets/img/web/hero\.webp[\"\']\s+alt=[\"\'][^\"\']*[\"\']\s+style=[\"\'][^\"\']*[\"\']\s+loading=[\"\']eager[\"\']\s*/>',
            re.DOTALL
        )
        hero_replacement = (
            '<img src="assets/img/web/hero.webp" alt="Kontraktor Bangunan Indonesia" '
            'width="600" height="600" fetchpriority="high" decoding="async" loading="eager" '
            'style="width: 100%; height: 100%; object-fit: cover; border-radius: 20px;" />'
        )
        new_content = hero_pattern.sub(hero_replacement, new_content)

    # 5. Add decoding="async" to lazy loaded images if missing
    new_content = re.sub(
        r'(<img\s+[^>]*loading=[\"\']lazy[\"\'])(?![^>]*decoding=)',
        r'\1 decoding="async"',
        new_content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return count > 0

def run():
    root_files = glob.glob('*.html')
    blog_files = glob.glob('blog/*.html')
    layanan_files = glob.glob('layanan/*.html')

    total_updated = 0
    for f in root_files:
        if optimize_html(f, is_sub=False):
            total_updated += 1
            print(f"Updated root: {f}")
        else:
            print(f"Manual check needed for: {f}")

    for f in blog_files:
        if optimize_html(f, is_sub=True):
            total_updated += 1

    for f in layanan_files:
        if optimize_html(f, is_sub=True):
            total_updated += 1

    print(f"Successfully processed {total_updated} files (out of {len(root_files) + len(blog_files) + len(layanan_files)} total).")

if __name__ == '__main__':
    run()
