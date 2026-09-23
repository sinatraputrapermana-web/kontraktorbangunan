import glob
import re

def update_file(fp, is_sub=False):
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()

    prefix = '../' if is_sub else ''

    # 1. Update Head: Replace fonts/bootstrap/icons block with ultra-lean non-blocking setup
    head_pattern = re.compile(
        r'<link\s+rel=[\"\']preconnect[\"\'][^>]*fonts\.googleapis\.com[^>]*>.*?'
        r'<link\s+rel=[\"\']stylesheet[\"\']\s+href=[\"\'][^\"\']*assets/css/style\.css[\"\']\s*/?>',
        re.DOTALL
    )

    if fp.endswith('index.html'):
        hero_preload = (
            f'<link rel="preload" as="image" href="{prefix}assets/img/web/hero-mobile.webp" media="(max-width: 600px)" fetchpriority="high" />\n'
            f'    <link rel="preload" as="image" href="{prefix}assets/img/web/hero.webp" media="(min-width: 601px)" fetchpriority="high" />\n'
        )
    else:
        hero_preload = ''

    new_head_links = (
        f'<link rel="preconnect" href="https://fonts.googleapis.com" />\n'
        f'    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />\n'
        f'    {hero_preload}'
        f'    <link rel="stylesheet" href="{prefix}assets/css/style.min.css" />\n'
        f'    <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" />\n'
        f'    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" media="print" onload="this.media=\'all\'" />\n'
        f'    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=Inter:wght@400;500;600;700&amp;display=swap" /></noscript>\n'
        f'    <link rel="preload" as="style" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" />\n'
        f'    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" media="print" onload="this.media=\'all\'" />\n'
        f'    <noscript><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" /></noscript>'
    )

    content = head_pattern.sub(new_head_links, content)

    # 2. Update bottom scripts: Remove bootstrap.bundle.min.js, use main.min.js
    script_pattern = re.compile(
        r'(<script\s+src=[\"\']https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.3/dist/js/bootstrap\.bundle\.min\.js[\"\'][^>]*>\s*</script>\s*)?'
        r'<script\s+src=[\"\'][^\"\']*assets/js/main(\.min)?\.js[\"\'][^>]*>\s*</script>',
        re.DOTALL
    )
    new_script = f'<script src="{prefix}assets/js/main.min.js" defer></script>'
    content = script_pattern.sub(new_script, content)

    # 3. For index.html: replace hero img with responsive picture tag
    if fp.endswith('index.html'):
        hero_img_pattern = re.compile(
            r'(<picture>.*?</picture>|<img\s+src=[\"\']assets/img/web/hero\.webp[\"\'][^>]*>)',
            re.DOTALL
        )
        responsive_hero = (
            '<picture>'
            '<source media="(max-width: 600px)" srcset="assets/img/web/hero-mobile.webp" type="image/webp" />'
            '<img src="assets/img/web/hero.webp" alt="Kontraktor Bangunan Indonesia" width="500" height="500" fetchpriority="high" decoding="async" loading="eager" style="width: 100%; height: auto; aspect-ratio: 1/1; object-fit: cover; border-radius: 20px;" />'
            '</picture>'
        )
        content = hero_img_pattern.sub(responsive_hero, content, count=1)

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    root_files = [f for f in glob.glob('*.html') if f != 'hubungi-kami.html']
    blog_files = glob.glob('blog/*.html')
    layanan_files = glob.glob('layanan/*.html')

    for f in root_files:
        update_file(f, is_sub=False)
        print("Updated root:", f)

    for f in blog_files:
        update_file(f, is_sub=True)

    for f in layanan_files:
        update_file(f, is_sub=True)

    print("All files updated successfully.")

if __name__ == '__main__':
    main()
