# Aturan Standar Pembuatan Halaman Artikel Blog

Setiap pembuatan atau pengeditan halaman detail artikel di `blog/*.html` **WAJIB** mengikuti panduan dan komponen terstandarisasi yang telah ditetapkan pada [STANDAR-LAYOUT-ARTIKEL.md](file:///c:/PROJECT/kontraktorbangunan/STANDAR-LAYOUT-ARTIKEL.md) serta menggunakan master template di [blog/template-artikel-master.html](file:///c:/PROJECT/kontraktorbangunan/blog/template-artikel-master.html).

### Ketentuan Mutlak:
1. **Layout 2 Kolom:** Wajib menggunakan layout `row g-5` dengan `col-lg-8` (konten artikel) dan `col-lg-4` (sidebar kanan).
2. **Komponen Wajib Konten (col-lg-8):**
   - `.scf-simple-breadcrumb` (Breadcrumb teks ringkas di kiri atas)
   - `.scf-article-h1` (Judul H1 fokus kata kunci)
   - `.scf-article-lead` (Paragraf pembuka / Answer Capsule)
   - `.scf-author-block` (Avatar, nama penulis, tanggal, estimasi baca, lencana reviewer LPJK)
   - `.scf-hero-photo` (16:9, border-radius 20px, cover) + `.scf-photo-caption`
   - `.scf-summary-box` (Ringkasan Inti dengan bullet points)
   - `.scf-toc-collapsible` (Daftar Isi interaktif yang bisa di-expand/collapse)
   - `.scf-tips-box` & `.scf-baca-juga-inline` (Komponen interaktif di sela pembahasan)
   - `.scf-comparison-table` dalam `.table-responsive`
   - `.scf-faq-accordion` (Accordion FAQ interaktif)
   - `.scf-conclusion-box` (Kesimpulan dengan 2 tombol CTA)
   - `.scf-author-profile-box` (Profil kartu penulis & reviewer di bawah)
   - `.scf-article-footer` (Tag artikel & tombol share WA/FB/Twitter)
3. **Komponen Wajib Sidebar (col-lg-4):**
   - `.scf-sidebar-cta` (Card WhatsApp CTA langsung)
   - `.scf-sidebar-card` Artikel Terkait (4 item dengan thumbnail, kategori, judul)
   - `.scf-sidebar-card` Layanan Pilihan (3 produk layanan unggulan)
4. **Skema SEO JSON-LD Lengkap:**
   - Wajib menyertakan `@graph` berisi `Article`, `BreadcrumbList`, `Product`/`Service`, dan `FAQPage`.
5. **Path Relatif:**
   - Semua path aset CSS, JS, dan gambar di dalam folder `blog/` wajib menggunakan `../assets/...`.
