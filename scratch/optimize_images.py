import os
from PIL import Image

def optimize_images():
    total_orig = 0
    total_new = 0
    optimized_count = 0

    for root, dirs, files in os.walk('assets/img'):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext not in ('.webp', '.jpg', '.jpeg', '.png'):
                continue
            fp = os.path.join(root, f)
            orig_size = os.path.getsize(fp)
            total_orig += orig_size
            try:
                with Image.open(fp) as im:
                    if f == 'favicon.jpeg':
                        im_small = im.copy()
                        if im_small.size[0] > 192 or im_small.size[1] > 192:
                            im_small.thumbnail((192, 192), Image.Resampling.LANCZOS)
                        im_small.convert('RGB').save(fp, 'JPEG', quality=85, optimize=True)
                    elif ext == '.webp':
                        # Resize if excessively large (e.g., > 1400px width)
                        w, h = im.size
                        if w > 1280:
                            new_h = int(h * (1280 / w))
                            im_resized = im.resize((1280, new_h), Image.Resampling.LANCZOS)
                        else:
                            im_resized = im
                        if im_resized.mode in ('RGBA', 'LA'):
                            im_resized.save(fp, 'WEBP', quality=82, method=6)
                        else:
                            im_resized.convert('RGB').save(fp, 'WEBP', quality=82, method=6)
                    elif ext in ('.jpg', '.jpeg'):
                        w, h = im.size
                        if w > 1280:
                            new_h = int(h * (1280 / w))
                            im_resized = im.resize((1280, new_h), Image.Resampling.LANCZOS)
                        else:
                            im_resized = im
                        im_resized.convert('RGB').save(fp, 'JPEG', quality=82, optimize=True)
                    elif ext == '.png':
                        im.save(fp, 'PNG', optimize=True)
                
                new_size = os.path.getsize(fp)
                total_new += new_size
                optimized_count += 1
                if orig_size - new_size > 20000 or orig_size > 150000:
                    print(f"Optimized {f}: {orig_size/1024:.1f}KB -> {new_size/1024:.1f}KB (saved {(orig_size-new_size)/1024:.1f}KB)")
            except Exception as e:
                print(f"Error {fp}: {e}")
                total_new += orig_size

    print(f"\nDone! Processed {optimized_count} images.")
    print(f"Total Original: {total_orig/1024/1024:.2f} MB")
    print(f"Total Optimized: {total_new/1024/1024:.2f} MB")
    print(f"Total Saved: {(total_orig - total_new)/1024/1024:.2f} MB")

if __name__ == '__main__':
    optimize_images()
