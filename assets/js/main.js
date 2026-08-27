document.addEventListener('DOMContentLoaded', function () {

  /* Mobile nav */
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.mobile-panel');
  var closeBtn = document.querySelector('.mobile-panel-close');
  
  var overlay = document.querySelector('.mobile-overlay');
  if (!overlay && panel) {
    overlay = document.createElement('div');
    overlay.className = 'mobile-overlay';
    document.body.appendChild(overlay);
  }

  function openMobileNav() {
    if (panel) panel.classList.add('open');
    if (overlay) overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMobileNav() {
    if (panel) panel.classList.remove('open');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (toggle) toggle.addEventListener('click', openMobileNav);
  if (closeBtn) closeBtn.addEventListener('click', closeMobileNav);
  if (overlay) overlay.addEventListener('click', closeMobileNav);

  /* Smooth Page Transitions & Navigation Link Handler */
  document.querySelectorAll('a[href]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = link.getAttribute('href');

      if (!href || 
          href.startsWith('#') || 
          href.startsWith('javascript:') || 
          href.startsWith('mailto:') || 
          href.startsWith('tel:') || 
          href.includes('wa.me') || 
          href.includes('api.whatsapp.com') || 
          link.getAttribute('target') === '_blank' ||
          e.metaKey || e.ctrlKey || e.shiftKey) {
        return;
      }

      e.preventDefault();
      
      if (panel && panel.classList.contains('open')) {
        closeMobileNav();
      }

      document.body.classList.add('page-is-exiting');

      setTimeout(function () {
        window.location.href = href;
      }, 200);
    });
  });

  window.addEventListener('pageshow', function (event) {
    document.body.classList.remove('page-is-exiting');
  });

  /* Mobile submenu accordion */
  document.querySelectorAll('.mobile-toggle-sub').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var sub = btn.nextElementSibling;
      var isOpen = btn.classList.contains('open');
      if (isOpen) {
        btn.classList.remove('open');
        sub.classList.remove('open');
        sub.style.maxHeight = null;
      } else {
        btn.classList.add('open');
        sub.classList.add('open');
        sub.style.maxHeight = sub.scrollHeight + 'px';
      }
    });
  });

  /* Auto-detect Active Mobile Page & Auto-expand Submenu */
  var currentPath = window.location.pathname;
  document.querySelectorAll('.mobile-links a, .mobile-sub a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (!href) return;
    
    var cleanHref = href.replace('../', '');
    if (currentPath.endsWith(cleanHref) || (cleanHref !== 'index.html' && currentPath.includes(cleanHref))) {
      link.classList.add('active');

      var parentSub = link.closest('.mobile-sub');
      if (parentSub) {
        parentSub.classList.add('open');
        parentSub.style.maxHeight = parentSub.scrollHeight + 'px';
        var parentToggle = parentSub.previousElementSibling;
        if (parentToggle && parentToggle.classList.contains('mobile-toggle-sub')) {
          parentToggle.classList.add('open', 'has-active');
        }
      }
    }
  });

  /* Scroll reveal */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('in'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.15 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* Number counters */
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var target = parseInt(el.getAttribute('data-count'), 10);
        var suffix = el.getAttribute('data-suffix') || '';
        var dur = 1400, start = null;
        function step(ts) {
          if (!start) start = ts;
          var progress = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.floor(eased * target) + suffix;
          if (progress < 1) requestAnimationFrame(step); else el.textContent = target + suffix;
        }
        requestAnimationFrame(step);
        cio.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* FAQ accordion */
  document.querySelectorAll('.faq-item').forEach(function (item) {
    var q = item.querySelector('.faq-q');
    var a = item.querySelector('.faq-a');
    q.addEventListener('click', function () {
      var isOpen = item.classList.contains('open');
      item.closest('.faq-list').querySelectorAll('.faq-item').forEach(function (i) {
        i.classList.remove('open');
        i.querySelector('.faq-a').style.maxHeight = null;
      });
      if (!isOpen) {
        item.classList.add('open');
        a.style.maxHeight = a.scrollHeight + 'px';
      }
    });
  });

  /* Portfolio / blog filter */
  document.querySelectorAll('.filter-bar').forEach(function (bar) {
    var targetSelector = bar.getAttribute('data-target');
    var items = document.querySelectorAll(targetSelector);
    bar.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        bar.querySelectorAll('button').forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.getAttribute('data-filter');
        items.forEach(function (it) {
          var show = (cat === 'all' || it.getAttribute('data-cat') === cat);
          it.style.display = show ? '' : 'none';
        });
      });
    });
  });

  /* Portfolio filter buttons (.portfolio-filter) */
  var pFilterBtns = document.querySelectorAll('.portfolio-filter .filter-btn');
  var pCards = document.querySelectorAll('.portfolio-grid .portfolio-card');
  if (pFilterBtns.length && pCards.length) {
    pFilterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        pFilterBtns.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        var cat = btn.getAttribute('data-filter');
        pCards.forEach(function (card) {
          var cardCat = card.getAttribute('data-cat');
          if (cat === 'all' || cardCat === cat) {
            card.style.display = 'block';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  /* Before/after slider */
  document.querySelectorAll('.ba-slider').forEach(function (slider) {
    var afterWrap = slider.querySelector('.ba-after-wrap');
    var handle = slider.querySelector('.ba-handle');
    var dragging = false;
    function setPos(clientX) {
      var rect = slider.getBoundingClientRect();
      var pct = Math.min(Math.max((clientX - rect.left) / rect.width, 0), 1);
      afterWrap.style.width = (pct * 100) + '%';
      handle.style.left = (pct * 100) + '%';
    }
    handle.addEventListener('mousedown', function () { dragging = true; });
    window.addEventListener('mouseup', function () { dragging = false; });
    window.addEventListener('mousemove', function (e) { if (dragging) setPos(e.clientX); });
    handle.addEventListener('touchstart', function () { dragging = true; }, { passive: true });
    window.addEventListener('touchend', function () { dragging = false; });
    window.addEventListener('touchmove', function (e) { if (dragging) setPos(e.touches[0].clientX); }, { passive: true });
  });

  /* Header animation on scroll */
  var header = document.querySelector('.site-header');
  if (header) {
    function checkScroll() {
      if (window.scrollY > 20) {
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', checkScroll, { passive: true });
    checkScroll();
  }

  /* Scroll to top button */
  var scrollTopBtn = document.createElement('button');
  scrollTopBtn.className = 'scroll-top-btn';
  scrollTopBtn.setAttribute('aria-label', 'Kembali ke atas');
  scrollTopBtn.innerHTML = '<i class="bi bi-arrow-up"></i>';
  document.body.appendChild(scrollTopBtn);

  function checkScrollTop() {
    if (window.scrollY > 250) {
      scrollTopBtn.classList.add('show');
    } else {
      scrollTopBtn.classList.remove('show');
    }
  }

  window.addEventListener('scroll', checkScrollTop, { passive: true });
  checkScrollTop();

  scrollTopBtn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* Gallery Modal Preview Handler */
  var gModal = document.getElementById('galleryModal');
  if (gModal) {
    gModal.addEventListener('show.bs.modal', function (event) {
      var button = event.relatedTarget;
      if (!button) return;
      var card = button.querySelector('.project-card-sleek') || button;
      var title = card.querySelector('h3') ? card.querySelector('h3').textContent : 'Detail Proyek';
      var cat = card.querySelector('.proj-cat-badge') ? card.querySelector('.proj-cat-badge').textContent : 'Portofolio';
      var meta = card.querySelector('.proj-meta') ? card.querySelector('.proj-meta').innerHTML : 'Indonesia';
      var imgEl = card.querySelector('.proj-img-wrap img');
      var phEl = card.querySelector('.ph');
      var label = phEl ? (phEl.getAttribute('data-label') || title) : title;

      document.getElementById('modalTitle').textContent = title;
      document.getElementById('modalCatBadge').textContent = cat;
      document.getElementById('modalMeta').innerHTML = meta;
      if (imgEl && imgEl.getAttribute('src')) {
        document.getElementById('modalImgContainer').innerHTML = '<img src="' + imgEl.getAttribute('src') + '" alt="' + title + '" style="width:100%;height:100%;object-fit:cover;aspect-ratio:16/10;">';
      } else {
        document.getElementById('modalImgContainer').innerHTML = '<div class="ph" data-label="' + label + '" style="width:100%;height:100%;aspect-ratio:16/10;"></div>';
      }
      
      var waUrl = 'https://wa.me/6288989643555?text=Halo%20Kontraktor%20Bangunan%2C%20saya%20tertarik%20dengan%20proyek%20' + encodeURIComponent(title) + '.';
      document.getElementById('modalWaBtn').setAttribute('href', waUrl);
    });
  }

  /* Article Reader Modal Handler */
  var aModal = document.getElementById('articleModal');
  if (aModal) {
    aModal.addEventListener('show.bs.modal', function (event) {
      var button = event.relatedTarget;
      if (!button) return;
      var card = button.querySelector('.blog-card-sleek') || button;
      var title = card.querySelector('h3') ? card.querySelector('h3').textContent : 'Artikel';
      var cat = card.querySelector('.blog-cat-pill') ? card.querySelector('.blog-cat-pill').textContent : 'Tips';
      var excerpt = card.querySelector('p') ? card.querySelector('p').textContent : '';

      document.getElementById('artModalTitle').textContent = title;
      document.getElementById('artModalCatBadge').textContent = cat;
      document.getElementById('artModalExcerpt').textContent = excerpt;
    });
  }

  /* Auto Rotating Mobile Stats Carousel */
  var statCards = document.querySelectorAll('.stats-carousel .stat-card');
  var statDots = document.querySelectorAll('.stats-dots .stat-dot');
  if (statCards.length > 0) {
    var statIndex = 0;
    setInterval(function () {
      if (window.innerWidth <= 767) {
        statCards[statIndex].classList.remove('active');
        if (statDots[statIndex]) statDots[statIndex].classList.remove('active');
        
        statIndex = (statIndex + 1) % statCards.length;
        
        statCards[statIndex].classList.add('active');
        if (statDots[statIndex]) statDots[statIndex].classList.add('active');
      }
    }, 2800);
  }
});
