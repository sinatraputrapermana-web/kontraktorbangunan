from PIL import Image

# 1. Create hero-mobile.webp (500x500, high quality, small size)
with Image.open('assets/img/web/hero.webp') as im:
    im_mobile = im.copy()
    im_mobile.thumbnail((500, 500), Image.Resampling.LANCZOS)
    im_mobile.save('assets/img/web/hero-mobile.webp', 'WEBP', quality=80, method=6)
    
    im_desktop = im.copy()
    im_desktop.thumbnail((800, 800), Image.Resampling.LANCZOS)
    im_desktop.save('assets/img/web/hero.webp', 'WEBP', quality=80, method=6)

# 2. Optimize tentang-kami.webp
with Image.open('assets/img/web/tentang-kami.webp') as im:
    im_small = im.copy()
    im_small.thumbnail((800, 600), Image.Resampling.LANCZOS)
    im_small.save('assets/img/web/tentang-kami.webp', 'WEBP', quality=80, method=6)

import os
print("hero-mobile.webp:", os.path.getsize('assets/img/web/hero-mobile.webp') / 1024, "KB")
print("hero.webp:", os.path.getsize('assets/img/web/hero.webp') / 1024, "KB")
print("tentang-kami.webp:", os.path.getsize('assets/img/web/tentang-kami.webp') / 1024, "KB")
