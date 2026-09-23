import os
import shutil
import re

# 1. Move markdown files (24, 25, 26 Sep) to stok/
md_files = [
    "artikel24september.md",
    "artikel25september.md",
    "artikel26september.md"
]

for mf in md_files:
    if os.path.exists(mf):
        shutil.move(mf, os.path.join("stok", mf))
        print(f"Moved {mf} -> stok/{mf}")

# 2. Move HTML files (24, 25, 26 Sep) from blog/ to stok/
html_files = [
    "jasa-renovasi-rumah-surabaya-terbaik.html",
    "biaya-renovasi-rumah-2-lantai-surabaya.html",
    "tips-renovasi-fasad-rumah-surabaya.html",
    "kontraktor-gedung-malang-bertingkat.html",
    "biaya-bangun-gedung-malang.html",
    "kontraktor-hotel-villa-malang-batu.html",
    "kontraktor-konstruksi-pabrik-gudang-pasuruan.html",
    "konstruksi-baja-wf-pasuruan.html",
    "biaya-konstruksi-bangunan-pasuruan.html"
]

for hf in html_files:
    src = os.path.join("blog", hf)
    if os.path.exists(src):
        shutil.move(src, os.path.join("stok", hf))
        print(f"Moved {src} -> stok/{hf}")

# 3. Adjust blog.html
with open("blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

# Define the 23 Sep cards that SHOULD be at the top
cards_23_sep = """        <!-- 23 Sep 2026 - JASA-ARSITEK-KEDIRI-DESAIN-RUMAH-MEWAH -->
        <div class="col-md-4 reveal">
          <a href="blog/jasa-arsitek-kediri-desain-rumah-mewah.html" class="blog-card-sleek">
            <div class="blog-img-wrap">
              <img src="assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-01.webp"
                alt="Jasa arsitek kediri desain rumah mewah modern tropis 2 lantai dengan bukaan kaca lebar" loading="lazy">
              <span class="blog-cat-pill">Jasa Arsitek</span>
            </div>
            <div class="blog-body">
              <h3>Jasa Arsitek Kediri Desain Rumah Mewah, Modern &amp; Tropis Bergaransi</h3>
              <p>Cari jasa arsitek Kediri terpercaya? Rancang desain rumah mewah, villa, tropis modern, DED lengkap &amp; pengurusan PBG. Konsultasi Desain &amp; RAB Gratis!</p>
              <div class="blog-footer-row">
                <span class="blog-meta-info"><i class="bi bi-calendar3 me-1"></i>23 Sep 2026 · <i
                    class="bi bi-clock me-1"></i>7 min</span>
                <span class="btn-read-blog">Baca Artikel</span>
              </div>
            </div>
          </a>
        </div>

        <!-- 23 Sep 2026 - BIAYA-JASA-ARSITEK-RUMAH-KEDIRI -->
        <div class="col-md-4 reveal">
          <a href="blog/biaya-jasa-arsitek-rumah-kediri.html" class="blog-card-sleek">
            <div class="blog-img-wrap">
              <img src="assets/img/blog/biaya-jasa-arsitek-rumah-kediri-01.webp"
                alt="Biaya jasa arsitek rumah kediri kalkulasi rancangan anggaran biaya rab dan dokumen ded" loading="lazy">
              <span class="blog-cat-pill">Arsitektur &amp; RAB</span>
            </div>
            <div class="blog-body">
              <h3>Rincian Biaya Jasa Arsitek Rumah di Kediri &amp; Tips Menghitung RAB</h3>
              <p>Simak rincian tarif biaya jasa arsitek rumah di Kediri terbaru 2026. Panduan hitung tarif per meter, persentase RAB &amp; cara hemat biaya. Cek infonya!</p>
              <div class="blog-footer-row">
                <span class="blog-meta-info"><i class="bi bi-calendar3 me-1"></i>23 Sep 2026 · <i
                    class="bi bi-clock me-1"></i>6 min</span>
                <span class="btn-read-blog">Baca Artikel</span>
              </div>
            </div>
          </a>
        </div>

        <!-- 23 Sep 2026 - JASA-ARSITEK-RUKO-KAFE-KEDIRI -->
        <div class="col-md-4 reveal">
          <a href="blog/jasa-arsitek-ruko-kafe-kediri.html" class="blog-card-sleek">
            <div class="blog-img-wrap">
              <img src="assets/img/blog/jasa-arsitek-ruko-kafe-kediri-01.webp"
                alt="Jasa arsitek ruko kafe kediri desain fasad modern industrial komersial instagramable" loading="lazy">
              <span class="blog-cat-pill">Desain Komersial</span>
            </div>
            <div class="blog-body">
              <h3>Jasa Desain Arsitek Ruko, Kafe &amp; Bangunan Komersial di Kediri</h3>
              <p>Cari jasa arsitek ruko &amp; kafe di Kediri? Desain fasad komersial modern, layout instagramable, DED lengkap &amp; izin usaha PBG. Konsultasi Desain Komersial!</p>
              <div class="blog-footer-row">
                <span class="blog-meta-info"><i class="bi bi-calendar3 me-1"></i>23 Sep 2026 · <i
                    class="bi bi-clock me-1"></i>7 min</span>
                <span class="btn-read-blog">Baca Artikel</span>
              </div>
            </div>
          </a>
        </div>
"""

# In blog.html, remove from <div class="row g-4"> up to the start of <!-- 22 september or <!-- 23 Sep
# Let's clean everything above 22 september and replace with 23 Sep cards
row_match = re.search(r'(<div class="row g-4">)(.*?)(<!-- 22 september)', blog_content, re.DOTALL)
if row_match:
    blog_content = blog_content[:row_match.start(1)] + '<div class="row g-4">\n\n' + cards_23_sep + '\n        ' + blog_content[row_match.start(3):]
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(blog_content)
    print("blog.html adjusted: only 23 Sep articles are active!")
else:
    print("Warning: regex pattern for blog.html not matched")

# 4. Adjust sitemap.xml
with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Update lastmod for blog index to 2026-09-23
sitemap_content = re.sub(
    r'(<loc>https://kontraktorbangunan\.web\.id/blog</loc>\s*<lastmod>)[^<]+(</lastmod>)',
    r'\g<1>2026-09-23\g<2>',
    sitemap_content
)

# 23 Sep sitemap entries
sitemap_23_sep = """  <!-- Blog Detail: jasa-arsitek-kediri-desain-rumah-mewah (23 Sep 2026) -->
  <url>
    <loc>https://kontraktorbangunan.web.id/blog/jasa-arsitek-kediri-desain-rumah-mewah</loc>
    <lastmod>2026-09-23</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-01.webp</image:loc>
      <image:title>Jasa arsitek kediri desain rumah mewah modern tropis 2 lantai dengan bukaan kaca lebar</image:title>
    </image:image>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-02.webp</image:loc>
      <image:title>Lembar cetak gambar kerja DED arsitektur dan simulasi visual 3D render rumah kediri</image:title>
    </image:image>
  </url>

  <!-- Blog Detail: biaya-jasa-arsitek-rumah-kediri (23 Sep 2026) -->
  <url>
    <loc>https://kontraktorbangunan.web.id/blog/biaya-jasa-arsitek-rumah-kediri</loc>
    <lastmod>2026-09-23</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/biaya-jasa-arsitek-rumah-kediri-01.webp</image:loc>
      <image:title>Biaya jasa arsitek rumah kediri kalkulasi rancangan anggaran biaya rab dan dokumen ded</image:title>
    </image:image>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-02.webp</image:loc>
      <image:title>Visualisasi 3d render arsitektur rumah modern minimalis 2 lantai di kediri</image:title>
    </image:image>
  </url>

  <!-- Blog Detail: jasa-arsitek-ruko-kafe-kediri (23 Sep 2026) -->
  <url>
    <loc>https://kontraktorbangunan.web.id/blog/jasa-arsitek-ruko-kafe-kediri</loc>
    <lastmod>2026-09-23</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/jasa-arsitek-ruko-kafe-kediri-01.webp</image:loc>
      <image:title>Jasa arsitek ruko kafe kediri desain fasad modern industrial komersial instagramable</image:title>
    </image:image>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/assets/img/blog/jasa-arsitek-ruko-kafe-kediri-02.webp</image:loc>
      <image:title>Layout interior kafe dan ruko komersial modern dengan pencahayaan estetik di kediri</image:title>
    </image:image>
  </url>
"""

# In sitemap.xml, replace from </url> after blog index up to the 22 Sep or 18 Sep entry
# Let's find blog index url close
blog_index_end = sitemap_content.find("https://kontraktorbangunan.web.id/blog</loc>")
if blog_index_end != -1:
    after_blog_index = sitemap_content.find("</url>", blog_index_end) + len("</url>\n")
    # Find next entry that is NOT 24, 25, 26, 23
    # Look for <!-- Blog Detail: Mengenal Jenis Genteng Tahan Bocor (18 Sep 2026) or 22 Sep
    target_match = re.search(r'(\s*<!-- Blog Detail:.*?18 Sep 2026)', sitemap_content)
    if target_match:
        target_idx = target_match.start()
        sitemap_content = sitemap_content[:after_blog_index] + sitemap_23_sep + "\n" + sitemap_content[target_idx:]
        with open("sitemap.xml", "w", encoding="utf-8") as f:
            f.write(sitemap_content)
        print("sitemap.xml adjusted: only 23 Sep (and published articles) are active!")
    else:
        print("Warning: target_match for sitemap not found")

print("Finished processing stok separation and site updates!")
