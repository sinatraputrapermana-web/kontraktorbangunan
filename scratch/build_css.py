import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

grid_utilities = """
/* ============================================================
   LIGHTWEIGHT GRID & UTILITIES (Eliminates Bootstrap 230KB CSS)
   ============================================================ */
.container,
.container-fluid,
.container-xl {
  width: 100%;
  max-width: var(--container-max, 1220px);
  margin-inline: auto;
  padding-inline: var(--gutter, 20px);
}

.row {
  --bs-gutter-x: 1.5rem;
  --bs-gutter-y: 0;
  display: flex;
  flex-wrap: wrap;
  margin-top: calc(-1 * var(--bs-gutter-y));
  margin-right: calc(-0.5 * var(--bs-gutter-x));
  margin-left: calc(-0.5 * var(--bs-gutter-x));
}

.row > * {
  flex-shrink: 0;
  width: 100%;
  max-width: 100%;
  padding-right: calc(var(--bs-gutter-x) * 0.5);
  padding-left: calc(var(--bs-gutter-x) * 0.5);
  margin-top: var(--bs-gutter-y);
}

.g-2 { --bs-gutter-x: 0.5rem; --bs-gutter-y: 0.5rem; }
.g-3 { --bs-gutter-x: 1rem; --bs-gutter-y: 1rem; }
.g-4 { --bs-gutter-x: 1.5rem; --bs-gutter-y: 1.5rem; }
.g-5 { --bs-gutter-x: 3rem; --bs-gutter-y: 3rem; }

.col-6 { flex: 0 0 auto; width: 50%; }
.col-12 { flex: 0 0 auto; width: 100%; }

@media (min-width: 768px) {
  .col-md-3 { flex: 0 0 auto; width: 25%; }
  .col-md-4 { flex: 0 0 auto; width: 33.33333333%; }
  .col-md-6 { flex: 0 0 auto; width: 50%; }
  .col-md-8 { flex: 0 0 auto; width: 66.66666667%; }
  .col-md-12 { flex: 0 0 auto; width: 100%; }
}

@media (min-width: 992px) {
  .col-lg-2 { flex: 0 0 auto; width: 16.66666667%; }
  .col-lg-3 { flex: 0 0 auto; width: 25%; }
  .col-lg-4 { flex: 0 0 auto; width: 33.33333333%; }
  .col-lg-6 { flex: 0 0 auto; width: 50%; }
  .col-lg-8 { flex: 0 0 auto; width: 66.66666667%; }
  .col-lg-12 { flex: 0 0 auto; width: 100%; }
}

.d-flex { display: flex !important; }
.d-inline-flex { display: inline-flex !important; }
.d-none { display: none !important; }
.d-block { display: block !important; }
.flex-column { flex-direction: column !important; }
.flex-wrap { flex-wrap: wrap !important; }
.align-items-center { align-items: center !important; }
.justify-content-center { justify-content: center !important; }
.justify-content-between { justify-content: space-between !important; }
.w-100 { width: 100% !important; }
.h-100 { height: 100% !important; }
.position-relative { position: relative !important; }
.position-absolute { position: absolute !important; }
.top-0 { top: 0 !important; }
.end-0 { right: 0 !important; }
.text-center { text-align: center !important; }
.text-muted { color: var(--c-muted, #77727A) !important; }
.text-white { color: #ffffff !important; }
.text-danger { color: #dc3545 !important; }
.text-success { color: #198754 !important; }
.fw-bold, .font-weight-bold { font-weight: 700 !important; }
.fw-semibold { font-weight: 600 !important; }
.rounded { border-radius: 8px !important; }
.rounded-3 { border-radius: 12px !important; }
.rounded-4 { border-radius: 16px !important; }
.rounded-pill { border-radius: 50rem !important; }
.border-0 { border: 0 !important; }
.p-0 { padding: 0 !important; }
.p-3 { padding: 1rem !important; }
.p-4 { padding: 1.5rem !important; }
.py-2 { padding-top: 0.5rem !important; padding-bottom: 0.5rem !important; }
.py-4 { padding-top: 1.5rem !important; padding-bottom: 1.5rem !important; }
.px-4 { padding-left: 1.5rem !important; padding-right: 1.5rem !important; }
.mb-0 { margin-bottom: 0 !important; }
.mb-1 { margin-bottom: 0.25rem !important; }
.mb-2 { margin-bottom: 0.5rem !important; }
.mb-3 { margin-bottom: 1rem !important; }
.mb-4 { margin-bottom: 1.5rem !important; }
.mt-2 { margin-top: 0.5rem !important; }
.mt-3 { margin-top: 1rem !important; }
.mt-4 { margin-top: 1.5rem !important; }
.mt-5 { margin-top: 3rem !important; }
.gap-2 { gap: 0.5rem !important; }
.gap-3 { gap: 1rem !important; }

.modal {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.65);
  z-index: 1050;
  overflow-x: hidden;
  overflow-y: auto;
  backdrop-filter: blur(4px);
}
.modal.show, .modal[style*="display: block"] {
  display: flex !important;
  align-items: center;
  justify-content: center;
}
.modal-dialog {
  position: relative;
  width: 90%;
  max-width: 600px;
  margin: 1.75rem auto;
}
.modal-dialog-centered {
  display: flex;
  align-items: center;
  min-height: calc(100% - 3.5rem);
}
.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: var(--c-milk, #F8F6F1);
  border: 1px solid var(--c-line, rgba(38,35,41,0.1));
  border-radius: 16px;
  overflow: hidden;
  box-shadow: var(--c-shadow, 0 24px 48px rgba(0,0,0,0.2));
}
.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.5rem;
  border-bottom: 1px solid var(--c-line, rgba(38,35,41,0.1));
}
.modal-body {
  position: relative;
  flex: 1 1 auto;
  padding: 1.5rem;
}
.modal-footer {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  padding: 1rem 1.5rem;
  border-top: 1px solid var(--c-line, rgba(38,35,41,0.1));
}
.btn-close, .btn-close-white {
  background: none;
  border: none;
  font-size: 1.5rem;
  line-height: 1;
  cursor: pointer;
  opacity: 0.7;
}
.btn-close:hover { opacity: 1; }
"""

full_css = css + "\n" + grid_utilities
with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(full_css)

# Generate minified CSS
min_css = re.sub(r'/\*[\s\S]*?\*/', '', full_css)
min_css = re.sub(r'\s+', ' ', min_css)
min_css = re.sub(r'\s*([\{\}:;,>+~])\s*', r'\1', min_css)
min_css = re.sub(r';\}', '}', min_css)
min_css = min_css.strip()

with open('assets/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(min_css)

print("Generated style.min.css:", len(min_css) / 1024, "KB")
