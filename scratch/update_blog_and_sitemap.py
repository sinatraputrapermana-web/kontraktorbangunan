import os
import re

# 12 articles data in reverse chronological order (26, 25, 24, 23 Sep)
new_articles = [
    # 26 Sep - Pasuruan
    {
        "date_ymd": "2026-09-26",
        "date_human": "26 Sep 2026",
        "read_time": "8 min",
        "category": "Pabrik &amp; Gudang",
        "slug": "kontraktor-konstruksi-pabrik-gudang-pasuruan",
        "title": "Jasa Kontraktor Konstruksi Pabrik &amp; Gudang di Kawasan Industri Pasuruan (PIER &amp; Beji)",
        "desc": "Cari jasa kontraktor konstruksi pabrik &amp; gudang di Pasuruan (PIER, Beji, Gempol)? Rangka baja WF SNI, lantai heavy duty, SLF &amp; izin PBG. Kirim RFP!",
        "img1": "assets/img/blog/kontraktor-konstruksi-pabrik-gudang-pasuruan-01.webp",
        "img1_alt": "Kontraktor konstruksi pasuruan pembangunan pabrik dan pergudangan industri baja bentang lebar",
        "img2": "assets/img/blog/kontraktor-konstruksi-pabrik-gudang-pasuruan-02.webp",
        "img2_alt": "Pemasangan rangka baja portal frame kolom wf dan pengecoran lantai industri pasuruan"
    },
    {
        "date_ymd": "2026-09-26",
        "date_human": "26 Sep 2026",
        "read_time": "7 min",
        "category": "Konstruksi Baja",
        "slug": "konstruksi-baja-wf-pasuruan",
        "title": "Jasa Konstruksi Baja WF &amp; Rancang Bangun Bangunan Industri di Pasuruan",
        "desc": "Jasa konstruksi baja WF di Pasuruan untuk pabrik, gudang, kanopi &amp; ruko. Fabrikasi presisi, baut high tensile &amp; garansi struktur SNI. Dapatkan RAB Gratis!",
        "img1": "assets/img/blog/konstruksi-baja-wf-pasuruan-01.webp",
        "img1_alt": "Konstruksi baja wf pasuruan perakitan portal frame rafter dan kolom pabrik industri",
        "img2": "assets/img/blog/konstruksi-baja-wf-pasuruan-02.webp",
        "img2_alt": "Detail sambungan baut mutu tinggi high tensile dan pelat simpul baja wf konstruksi pasuruan"
    },
    {
        "date_ymd": "2026-09-26",
        "date_human": "26 Sep 2026",
        "read_time": "7 min",
        "category": "Infrastruktur &amp; Sipil",
        "slug": "biaya-konstruksi-bangunan-pasuruan",
        "title": "Estimasi Biaya Konstruksi Bangunan Gedung &amp; Infrastruktur di Pasuruan",
        "desc": "Cek rincian estimasi biaya konstruksi bangunan &amp; infrastruktur di Pasuruan terbaru 2026. Panduan hitung RAB pabrik, gedung, perumahan &amp; izin PBG.",
        "img1": "assets/img/blog/biaya-konstruksi-bangunan-pasuruan-01.webp",
        "img1_alt": "Biaya konstruksi pasuruan kalkulasi rencana anggaran biaya rab bangunan gedung dan fasilitas sipil",
        "img2": "assets/img/blog/biaya-konstruksi-bangunan-pasuruan-02.webp",
        "img2_alt": "Pekerjaan pemadatan jalan beton rigit pavement dan drainase saluran kawasan industri pasuruan"
    },

    # 25 Sep - Malang
    {
        "date_ymd": "2026-09-25",
        "date_human": "25 Sep 2026",
        "read_time": "8 min",
        "category": "Gedung Bertingkat",
        "slug": "kontraktor-gedung-malang-bertingkat",
        "title": "Jasa Kontraktor Gedung Bertingkat Malang (Kantor, Kampus &amp; Komersial)",
        "desc": "Cari jasa kontraktor gedung di Malang? Bangun gedung kantor, kampus, ruko, hotel &amp; fasilitas komersial. Struktur tahan gempa &amp; izin PBG/SLF. Kirim RFP!",
        "img1": "assets/img/blog/kontraktor-gedung-malang-bertingkat-01.webp",
        "img1_alt": "Kontraktor gedung malang konstruksi gedung kantor bertingkat modern struktur beton dan kaca",
        "img2": "assets/img/blog/kontraktor-gedung-malang-bertingkat-02.webp",
        "img2_alt": "Pekerjaan pengecoran plat lantai dan kolom beton bertulang gedung komersial malang"
    },
    {
        "date_ymd": "2026-09-25",
        "date_human": "25 Sep 2026",
        "read_time": "8 min",
        "category": "Biaya Gedung",
        "slug": "biaya-bangun-gedung-malang",
        "title": "Estimasi Rincian Biaya Bangun Gedung di Malang &amp; Standar Struktur Tahan Gempa",
        "desc": "Cek estimasi rincian biaya bangun gedung di Malang per meter persegi. Panduan struktur tahan gempa SNI, pondasi bored pile &amp; efisiensi RAB. Konsultasi WA!",
        "img1": "assets/img/blog/biaya-bangun-gedung-malang-01.webp",
        "img1_alt": "Biaya bangun gedung malang perhitungan struktur tahan gempa dan lembar rab konstruksi",
        "img2": "assets/img/blog/biaya-bangun-gedung-malang-02.webp",
        "img2_alt": "Pengujian beban tanah geoteknik dan pengeboran pondasi bored pile gedung bertingkat malang"
    },
    {
        "date_ymd": "2026-09-25",
        "date_human": "25 Sep 2026",
        "read_time": "8 min",
        "category": "Villa &amp; Resort",
        "slug": "kontraktor-hotel-villa-malang-batu",
        "title": "Kontraktor Bangunan Hotel, Villa &amp; Resort di Malang Raya &amp; Batu",
        "desc": "Jasa kontraktor hotel, villa &amp; resort di Malang Raya &amp; Kota Batu. Rancang bangun arsitektur tropis modern, infinity pool &amp; legalitas PBG. Konsultasi Proyek!",
        "img1": "assets/img/blog/kontraktor-hotel-villa-malang-batu-01.webp",
        "img1_alt": "Kontraktor villa malang batu desain villa resort mewah modern dengan infinity pool pemandangan bukit",
        "img2": "assets/img/blog/kontraktor-hotel-villa-malang-batu-02.webp",
        "img2_alt": "Pekerjaan retaining wall dinding penahan tanah dan struktur beton bertulang villa lereng batu"
    },

    # 24 Sep - Surabaya
    {
        "date_ymd": "2026-09-24",
        "date_human": "24 Sep 2026",
        "read_time": "8 min",
        "category": "Renovasi Rumah",
        "slug": "jasa-renovasi-rumah-surabaya-terbaik",
        "title": "Jasa Renovasi Rumah Surabaya Terbaik, Murah &amp; Bergaransi Resmi",
        "desc": "Cari jasa renovasi rumah Surabaya terbaik &amp; bergaransi? Renovasi total, tambah lantai, perbaikan atap bocor, RAB transparan. Konsultasi &amp; Survei Gratis!",
        "img1": "assets/img/blog/jasa-renovasi-rumah-surabaya-terbaik-01.webp",
        "img1_alt": "Jasa renovasi rumah surabaya renovasi fasad modern tropis dan interior rumah tinggal",
        "img2": "assets/img/blog/jasa-renovasi-rumah-surabaya-terbaik-02.webp",
        "img2_alt": "Pekerjaan pembongkaran dinding dan suntik pondasi cakar ayam renovasi rumah surabaya"
    },
    {
        "date_ymd": "2026-09-24",
        "date_human": "24 Sep 2026",
        "read_time": "8 min",
        "category": "Tambah Lantai 2",
        "slug": "biaya-renovasi-rumah-2-lantai-surabaya",
        "title": "Estimasi Biaya Renovasi Rumah 2 Lantai di Surabaya: Cara Suntik Pondasi &amp; Dak Beton",
        "desc": "Rincian estimasi biaya renovasi rumah 1 lantai jadi 2 lantai di Surabaya. Panduan metode suntik pondasi cakar ayam, dak beton keraton &amp; hebel. Cek RAB!",
        "img1": "assets/img/blog/biaya-renovasi-rumah-2-lantai-surabaya-01.webp",
        "img1_alt": "Biaya renovasi rumah 2 lantai surabaya metode suntik pondasi cakar ayam dan dak beton bertulang",
        "img2": "assets/img/blog/biaya-renovasi-rumah-2-lantai-surabaya-02.webp",
        "img2_alt": "Pengecoran plat lantai dak beton bondek lantai 2 rumah tinggal di surabaya"
    },
    {
        "date_ymd": "2026-09-24",
        "date_human": "24 Sep 2026",
        "read_time": "7 min",
        "category": "Fasad &amp; Eksterior",
        "slug": "tips-renovasi-fasad-rumah-surabaya",
        "title": "Tips Renovasi Fasad Rumah Minimalis Modern Tropis di Surabaya",
        "desc": "Mau ubah tampilan depan rumah? Simak tips renovasi fasad rumah Surabaya bergaya modern tropis, material tahan panas pesisir &amp; hemat biaya. Konsultasi WA!",
        "img1": "assets/img/blog/tips-renovasi-fasad-rumah-surabaya-01.webp",
        "img1_alt": "Renovasi fasad rumah surabaya modern tropis dengan aksen conwood batu alam dan kisi kisi",
        "img2": "assets/img/blog/tips-renovasi-fasad-rumah-surabaya-02.webp",
        "img2_alt": "Pemasangan kisi kisi louver aluminium dan cat eksterior elastomeric fasad rumah surabaya"
    },

    # 23 Sep - Kediri
    {
        "date_ymd": "2026-09-23",
        "date_human": "23 Sep 2026",
        "read_time": "7 min",
        "category": "Jasa Arsitek",
        "slug": "jasa-arsitek-kediri-desain-rumah-mewah",
        "title": "Jasa Arsitek Kediri Desain Rumah Mewah, Modern &amp; Tropis Bergaransi",
        "desc": "Cari jasa arsitek Kediri terpercaya? Rancang desain rumah mewah, villa, tropis modern, DED lengkap &amp; pengurusan PBG. Konsultasi Desain &amp; RAB Gratis!",
        "img1": "assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-01.webp",
        "img1_alt": "Jasa arsitek kediri desain rumah mewah modern tropis 2 lantai dengan bukaan kaca lebar",
        "img2": "assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-02.webp",
        "img2_alt": "Lembar cetak gambar kerja DED arsitektur dan simulasi visual 3D render rumah kediri"
    },
    {
        "date_ymd": "2026-09-23",
        "date_human": "23 Sep 2026",
        "read_time": "6 min",
        "category": "Arsitektur &amp; RAB",
        "slug": "biaya-jasa-arsitek-rumah-kediri",
        "title": "Rincian Biaya Jasa Arsitek Rumah di Kediri &amp; Tips Menghitung RAB",
        "desc": "Simak rincian tarif biaya jasa arsitek rumah di Kediri terbaru 2026. Panduan hitung tarif per meter, persentase RAB &amp; cara hemat biaya. Cek infonya!",
        "img1": "assets/img/blog/biaya-jasa-arsitek-rumah-kediri-01.webp",
        "img1_alt": "Biaya jasa arsitek rumah kediri kalkulasi rancangan anggaran biaya rab dan dokumen ded",
        "img2": "assets/img/blog/jasa-arsitek-kediri-desain-rumah-mewah-02.webp",
        "img2_alt": "Visualisasi 3d render arsitektur rumah modern minimalis 2 lantai di kediri"
    },
    {
        "date_ymd": "2026-09-23",
        "date_human": "23 Sep 2026",
        "read_time": "7 min",
        "category": "Desain Komersial",
        "slug": "jasa-arsitek-ruko-kafe-kediri",
        "title": "Jasa Desain Arsitek Ruko, Kafe &amp; Bangunan Komersial di Kediri",
        "desc": "Cari jasa arsitek ruko &amp; kafe di Kediri? Desain fasad komersial modern, layout instagramable, DED lengkap &amp; izin usaha PBG. Konsultasi Desain Komersial!",
        "img1": "assets/img/blog/jasa-arsitek-ruko-kafe-kediri-01.webp",
        "img1_alt": "Jasa arsitek ruko kafe kediri desain fasad modern industrial komersial instagramable",
        "img2": "assets/img/blog/jasa-arsitek-ruko-kafe-kediri-02.webp",
        "img2_alt": "Layout interior kafe dan ruko komersial modern dengan pencahayaan estetik di kediri"
    }
]

# Generate cards HTML for blog.html
cards_html = ""
for art in new_articles:
    cards_html += f"""        <!-- {art['date_human']} - {art['slug'].upper()} -->
        <div class="col-md-4 reveal">
          <a href="blog/{art['slug']}.html" class="blog-card-sleek">
            <div class="blog-img-wrap">
              <img src="{art['img1']}"
                alt="{art['img1_alt']}" loading="lazy">
              <span class="blog-cat-pill">{art['category']}</span>
            </div>
            <div class="blog-body">
              <h3>{art['title']}</h3>
              <p>{art['desc']}</p>
              <div class="blog-footer-row">
                <span class="blog-meta-info"><i class="bi bi-calendar3 me-1"></i>{art['date_human']} · <i
                    class="bi bi-clock me-1"></i>{art['read_time']}</span>
                <span class="btn-read-blog">Baca Artikel</span>
              </div>
            </div>
          </a>
        </div>

"""

# 1. Update blog.html
with open("blog.html", "r", encoding="utf-8") as f:
    blog_content = f.read()

# Target insertion point: right after `<div class="row g-4">`
target_str = '<div class="row g-4">\n'
if target_str in blog_content:
    updated_blog = blog_content.replace(target_str, target_str + "\n" + cards_html, 1)
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(updated_blog)
    print("blog.html updated with 12 new article cards successfully!")
else:
    print("Warning: <div class=\"row g-4\"> not found in blog.html")

# 2. Update sitemap.xml
# Generate sitemap entries for all 12 articles
sitemap_entries = ""
for art in new_articles:
    sitemap_entries += f"""  <!-- Blog Detail: {art['slug']} ({art['date_human']}) -->
  <url>
    <loc>https://kontraktorbangunan.web.id/blog/{art['slug']}</loc>
    <lastmod>{art['date_ymd']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/{art['img1']}</image:loc>
      <image:title>{art['img1_alt']}</image:title>
    </image:image>
    <image:image>
      <image:loc>https://kontraktorbangunan.web.id/{art['img2']}</image:loc>
      <image:title>{art['img2_alt']}</image:title>
    </image:image>
  </url>

"""

with open("sitemap.xml", "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Update lastmod of blog index in sitemap.xml
sitemap_content = re.sub(
    r'(<loc>https://kontraktorbangunan\.web\.id/blog</loc>\s*<lastmod>)[^<]+(</lastmod>)',
    r'\g<1>2026-09-26\g<2>',
    sitemap_content
)

# Insert new entries right after `<!-- Blog Detail:` of the first article or after `<loc>https://kontraktorbangunan.web.id/blog</loc>...</url>`
# Let's find `  <!-- Blog Detail:`
insert_match = re.search(r'(\s*<!-- Blog Detail:)', sitemap_content)
if insert_match:
    idx = insert_match.start()
    updated_sitemap = sitemap_content[:idx] + "\n" + sitemap_entries + sitemap_content[idx:]
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(updated_sitemap)
    print("sitemap.xml updated with 12 new article URLs successfully!")
else:
    print("Warning: Could not find insertion point in sitemap.xml")
