# Panduan Standar Desain & Layout Detail Artikel (Kontraktor Bangunan)

Dokumen ini adalah acuan resmi (**Standard Operating Procedure**) untuk memastikan seluruh halaman detail artikel di `blog/*.html` memiliki tampilan, struktur visual, elemen SEO, dan pengalaman pengguna yang **100% konsisten, profesional, dan seragam**.

---

## 1. Master Template File
File master acuan yang siap digunakan dan diduplikasi:
* **HTML Master Template:** [`blog/template-artikel-master.html`](file:///c:/PROJECT/kontraktorbangunan/blog/template-artikel-master.html)
* **Contoh Implementasi Sempurna:** [`blog/contoh-gambar-kerja-rumah-minimalis.html`](file:///c:/PROJECT/kontraktorbangunan/blog/contoh-gambar-kerja-rumah-minimalis.html)
* **File CSS Utama:** [`assets/css/style.css`](file:///c:/PROJECT/kontraktorbangunan/assets/css/style.css)

---

## 2. Struktur Anatomi Halaman Artikel

Setiap halaman artikel wajib mengikuti hierarki berikut:

```
├── <head> (SEO Meta Tags, OpenGraph, Twitter, Font Plus Jakarta Sans & Inter, Bootstrap 5.3.3, JSON-LD Schema)
├── <header class="site-header"> (Navbar Standar dengan link ../)
├── <div class="mobile-panel"> (Menu Drawer Mobile)
├── <main class="flex-grow-1 pt-4 pb-5 mb-4">
│   └── <div class="container-xl">
│       └── <div class="scf-article-page">
│           └── <div class="row g-5">
│               ├── <div class="col-lg-8"> (KONTEN UTAMA)
│               │   ├── 1. Breadcrumb Sederhana (.scf-simple-breadcrumb)
│               │   ├── 2. H1 Title (.scf-article-h1)
│               │   ├── 3. Lead Paragraph (.scf-article-lead)
│               │   ├── 4. Author Header (.scf-author-block)
│               │   ├── 5. Hero Image 16:9 + Caption (.scf-hero-photo + .scf-photo-caption)
│               │   ├── 6. Paragraf Pengantar
│               │   ├── 7. Ringkasan Inti (.scf-summary-box)
│               │   ├── 8. Daftar Isi Collapsible (.scf-toc-collapsible)
│               │   ├── 9. Body Artikel (.scf-article-body)
│               │   │   ├── H2 Section Headers + Bold Answer Lead
│               │   │   ├── Paragraf Isi & Data Statistik
│               │   │   ├── Tips Box (.scf-tips-box)
│               │   │   ├── Inline "Baca Juga" (.scf-baca-juga-inline)
│               │   │   ├── Foto Sekunder 16:9 + Caption
│               │   │   ├── Tabel Komparasi Responsif (.scf-comparison-table)
│               │   │   ├── FAQ Accordion Interaktif (.scf-faq-accordion)
│               │   │   ├── Kesimpulan Praktis + 2 CTA Buttons (.scf-conclusion-box)
│               │   │   ├── Profil Penulis & Reviewer (.scf-author-profile-box)
│               │   │   └── Tags & Tombol Share Medsos (.scf-article-footer)
│               │
│               └── <div class="col-lg-4"> (SIDEBAR KANAN)
│                   └── <aside class="scf-sidebar">
│                       ├── 1. CTA Box Konsultasi WhatsApp (.scf-sidebar-cta)
│                       ├── 2. Artikel Terkait (.scf-sidebar-card)
│                       └── 3. Layanan Pilihan (.scf-sidebar-card)
│
├── <footer class="site-footer"> (Footer 4 Kolom)
├── <a class="wa-float"> (Floating WhatsApp Button)
└── <script> (Bootstrap JS, main.js, TOC Chevron Handler)
```

---

## 3. Kamus Komponen & Kode Standar (Snippets)

### A. Breadcrumb Sederhana
```html
<nav aria-label="breadcrumb" class="scf-simple-breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="../index.html">Beranda</a></li>
    <li class="breadcrumb-item"><a href="../blog.html">Blog</a></li>
    <li class="breadcrumb-item active" aria-current="page">Judul Singkat Artikel</li>
  </ol>
</nav>
```

### B. Header Penulis & Reviewer (Atas)
```html
<div class="scf-author-block">
  <img src="../assets/img/blog/ardhana.jpeg" alt="Tim Spesialis Kontraktor Bangunan" class="scf-author-photo" />
  <div>
    <div class="scf-author-name">Tim Spesialis Kontraktor Bangunan</div>
    <div class="scf-author-meta">
      <span class="meta-item"><i class="bi bi-calendar3"></i> 10 September 2026</span>
      <span class="meta-item"><i class="bi bi-clock"></i> 7 menit baca</span>
      <span class="meta-item"><i class="bi bi-patch-check-fill text-purple"></i> Direview oleh Lembaga Pengembang Jasa Konstruksi</span>
    </div>
  </div>
</div>
```

### C. Hero & Foto Sekunder (Aspect Ratio 16:9)
```html
<img src="../assets/img/blog/slug-gambar-01.webp"
  alt="Deskripsi gambar SEO friendly"
  class="scf-hero-photo"
  style="width: 100%; aspect-ratio: 16/9; object-fit: cover; border-radius: 20px; margin-bottom: 12px;"
  loading="eager" />
<p class="scf-photo-caption">
  Keterangan penjelasan foto yang informatif dan relevan dengan konteks.
</p>
```

### D. Ringkasan Inti (Summary Box)
```html
<div class="scf-summary-box">
  <div class="scf-summary-label">
    <i class="bi bi-card-checklist"></i> Ringkasan Inti
  </div>
  <ul>
    <li><strong>Poin Kunci 1:</strong> Deskripsi ringkas intisari topik.</li>
    <li><strong>Poin Kunci 2:</strong> Data atau standar penting yang harus diperhatikan.</li>
    <li><strong>Poin Kunci 3:</strong> Solusi dan kepatuhan terhadap regulasi terkait.</li>
  </ul>
</div>
```

### E. Daftar Isi Collapsible (TOC)
```html
<div class="scf-toc-collapsible">
  <button class="scf-toc-toggle collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#tocBody"
    aria-expanded="false" aria-controls="tocBody" id="tocToggleBtn">
    <span class="scf-toc-toggle-label"><i class="bi bi-list-task"></i> Daftar Isi Artikel</span>
    <i class="bi bi-chevron-down scf-toc-chevron"></i>
  </button>
  <div class="collapse" id="tocBody">
    <div class="scf-toc-body">
      <ol>
        <li><a href="#id-bagian-1">Judul Sub-Topik 1</a></li>
        <li><a href="#id-bagian-2">Judul Sub-Topik 2</a></li>
        <li><a href="#faq">Pertanyaan yang Sering Diajukan (FAQ)</a></li>
        <li><a href="#kesimpulan">Kesimpulan Praktis</a></li>
        <li><a href="#penulis">Tentang Penulis &amp; Reviewer</a></li>
      </ol>
    </div>
  </div>
</div>
```

### F. Tips / Checklist Box
```html
<div class="scf-tips-box">
  <div class="scf-tips-label">
    <i class="bi bi-file-earmark-ruled"></i> Tips &amp; Panduan Teknis
  </div>
  <ul>
    <li><strong>Poin A:</strong> Penjelasan panduan praktis pertama.</li>
    <li><strong>Poin B:</strong> Penjelasan panduan praktis kedua.</li>
  </ul>
</div>
```

### G. Komponen Baca Juga Inline
```html
<div class="scf-baca-juga-inline">
  <div class="scf-baca-juga-inline-label"><i class="bi bi-book-half"></i> Baca Juga</div>
  <ul class="scf-baca-juga-inline-list">
    <li><a href="artikel-1.html"><i class="bi bi-arrow-right-short"></i> Judul Artikel Terkait 1</a></li>
    <li><a href="artikel-2.html"><i class="bi bi-arrow-right-short"></i> Judul Artikel Terkait 2</a></li>
  </ul>
</div>
```

### H. Tabel Komparasi Responsif
```html
<div class="table-responsive my-4">
  <table class="table table-striped scf-comparison-table">
    <thead>
      <tr>
        <th>Parameter Evaluasi</th>
        <th>Metode Konvensional</th>
        <th>Standar Kontraktor Bangunan</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Aspek Teknis 1</strong></td>
        <td>Keterangan varian standar</td>
        <td>Keterangan standar unggulan bersertifikat</td>
      </tr>
    </tbody>
  </table>
</div>
```

### I. FAQ Accordion
```html
<div class="scf-faq-accordion">
  <div class="scf-faq-item">
    <button class="scf-faq-toggle" type="button" data-bs-toggle="collapse" data-bs-target="#faq1" aria-expanded="false">
      Pertanyaan yang Sering Ditanyakan?
      <i class="bi bi-chevron-down scf-faq-chevron"></i>
    </button>
    <div class="collapse" id="faq1">
      <div class="scf-faq-body">
        Jawaban mendalam dan lengkap untuk pertanyaan tersebut.
      </div>
    </div>
  </div>
</div>
```

### J. Kesimpulan Box dengan 2 Tombol CTA
```html
<div class="scf-conclusion-box text-center" id="kesimpulan">
  <h2>Kesimpulan Praktis</h2>
  <p>Ringkasan akhir dan rekomendasi tindakan strategis bagi pembaca.</p>
  <div class="d-flex flex-wrap justify-content-center gap-3 mt-4">
    <a href="https://wa.me/6288989643555?text=Halo%20Kontraktor%20Bangunan%2C%20saya%20ingin%20konsultasi%20gratis."
      target="_blank" rel="noopener" class="scf-btn-success d-inline-flex align-items-center gap-2">
      <i class="bi bi-whatsapp"></i> Konsultasi Desain &amp; RAB Gratis
    </a>
    <a href="https://wa.me/6288989643555?text=Halo%20Kontraktor%20Bangunan%2C%20saya%20ingin%20minta%20portofolio."
      target="_blank" rel="noopener" class="scf-btn-outline-light d-inline-flex align-items-center gap-2">
      <i class="bi bi-file-earmark-ruled"></i> Minta Contoh Portofolio
    </a>
  </div>
</div>
```

### K. Profil Penulis & Reviewer Lengkap (Bawah)
```html
<div class="scf-author-profile-box" id="penulis">
  <div class="scf-author-profile-card">
    <div class="scf-author-profile-avatar-wrap">
      <img src="../assets/img/blog/ardhana.jpeg" alt="Tim Spesialis Kontraktor Bangunan" class="scf-author-profile-avatar" />
      <span class="scf-author-verified-badge" title="Terverifikasi"><i class="bi bi-patch-check-fill"></i></span>
    </div>
    <div class="scf-author-profile-info">
      <div class="scf-author-profile-header">
        <span class="scf-author-label">Penulis</span>
        <h4 class="scf-author-profile-name">Tim Spesialis Kontraktor Bangunan</h4>
      </div>
      <p class="scf-author-profile-bio">
        Praktisi perancangan arsitektur, rekayasa sipil struktur, dan spesialis penyusunan berkas Detail Engineering Design (DED) serta perizinan PBG di Indonesia.
      </p>
      <div class="scf-author-meta-extra mt-2" style="font-size: 0.82rem; color: var(--c-muted);">
        <span><i class="bi bi-shield-check text-purple"></i> Direview oleh: <strong>Lembaga Pengembangan Jasa Konstruksi</strong></span>
        <span class="ms-3"><i class="bi bi-journal-text text-purple"></i> Sumber: LPJK &amp; Tata Ruang Bangunan 2025/2026</span>
      </div>
    </div>
  </div>
</div>
```

---

## 4. Panduan Konversi dari Markdown (`articles/*.md`) ke HTML (`blog/*.html`)

| Bagian di Markdown (`.md`) | Dikonversi Menjadi Elemen HTML (`.html`) |
| :--- | :--- |
| `Meta Title` | `<title>`, `og:title`, `twitter:title`, `headline` di Schema |
| `Meta Description` | `<meta name="description">`, `og:description`, `twitter:description` |
| `Slug` | `<link rel="canonical" href=".../blog/{slug}">`, breadcrumb url, JSON-LD `@id` |
| `Images` (Gambar 1 & 2) | Hero Photo & Foto Sekunder dengan style `16/9; object-fit: cover; border-radius: 20px;` |
| `ANSWER CAPSULE` | Paragraf `<p class="scf-article-lead">` di bawah H1 |
| `Ringkasan Inti` | `<div class="scf-summary-box">` |
| `Daftar Isi` | `<div class="scf-toc-collapsible">` dengan link anchor ID |
| `## Heading 2` | `<h2 id="slug-anchor">` dengan `<strong>` direct answer di bawahnya |
| `Tabel Perbandingan` | `<div class="table-responsive"><table class="scf-comparison-table">` |
| `FAQ / Pertanyaan` | `<div class="scf-faq-accordion">` + Schema JSON-LD `FAQPage` |
| `Kesimpulan` | `<div class="scf-conclusion-box">` dengan 2 tombol CTA hijau & putih |

---

## 5. Checklist Verifikasi Sebelum Publish

- [ ] File disimpan di folder `blog/{slug}.html`.
- [ ] Path aset CSS/JS/Gambar menggunakan `../assets/` (karena berada di dalam subfolder `blog/`).
- [ ] Tag `<link rel="canonical">` mengarah ke URL lengkap artikel.
- [ ] Schema JSON-LD mencakup 4 entitas: `Article`, `BreadcrumbList`, `Product`/`Service`, dan `FAQPage`.
- [ ] Seluruh gambar memiliki atribut `alt` yang deskriptif dan inline style `aspect-ratio: 16/9; border-radius: 20px;`.
- [ ] ID Anchor pada Daftar Isi (TOC) cocok dengan atribut `id="..."` pada setiap `<h2>`.
- [ ] Link CTA WhatsApp sudah menyertakan pesan otomatis sesuai topik artikel.
- [ ] Tombol share (WhatsApp, Facebook, Twitter) terkonfigurasi dengan URL artikel aktif.
