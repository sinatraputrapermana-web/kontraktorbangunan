import os
from PIL import Image

src_dir = "assets/img/gambar_artikel"
dst_blog_dir = "assets/img/blog"

os.makedirs(src_dir, exist_ok=True)
os.makedirs(dst_blog_dir, exist_ok=True)

files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpeg', '.jpg'))]

print(f"Found {len(files)} JPEG files in {src_dir}")

for f in files:
    src_path = os.path.join(src_dir, f)
    base_name = os.path.splitext(f)[0]
    
    with Image.open(src_path) as img:
        # Convert to RGB if in RGBA or other modes
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        # Max dimensions for blog hero / secondary image: width 1200px max
        max_width = 1200
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int(float(img.height) * float(ratio))
            img_resized = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
        else:
            img_resized = img.copy()
        
        # Target size < 100KB (aiming for 60KB-90KB)
        # We try quality from 85 down to 50
        quality = 85
        temp_out = os.path.join(src_dir, f"{base_name}.webp")
        
        while quality >= 30:
            img_resized.save(temp_out, "WEBP", quality=quality, method=6)
            size = os.path.getsize(temp_out)
            if size < 95 * 1024:  # under 95KB
                break
            quality -= 5
        
        final_size_kb = os.path.getsize(temp_out) / 1024.0
        print(f"Converted {f} -> {base_name}.webp (Quality: {quality}, Size: {final_size_kb:.2f} KB)")
        
        # Copy to assets/img/blog as well
        blog_out = os.path.join(dst_blog_dir, f"{base_name}.webp")
        img_resized.save(blog_out, "WEBP", quality=quality, method=6)
        
        # Special handling if name is kontraktor-hotel-villa-malang-batu-03
        if base_name == "kontraktor-hotel-villa-malang-batu-03":
            alias_blog = os.path.join(dst_blog_dir, "kontraktor-hotel-villa-malang-batu-02.webp")
            alias_src = os.path.join(src_dir, "kontraktor-hotel-villa-malang-batu-02.webp")
            img_resized.save(alias_blog, "WEBP", quality=quality, method=6)
            img_resized.save(alias_src, "WEBP", quality=quality, method=6)
            print(f"Created alias: kontraktor-hotel-villa-malang-batu-02.webp")

print("All images converted and placed in assets/img/gambar_artikel and assets/img/blog successfully!")
