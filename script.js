/* ================================================
   GMB Services LLC — script.js
   Features: Preloader · Navbar · Smooth scroll
             Scroll reveal · Active nav tracking
             Animated counters · Back to top
             Hamburger menu · Form validation
   ================================================ */

(function () {
  'use strict';

  /* ============ PRELOADER ============ */
  window.addEventListener('load', function () {
    const preloader = document.getElementById('preloader');
    if (!preloader) return;
    setTimeout(function () {
      preloader.classList.add('hidden');
      setTimeout(function () {
        preloader.style.display = 'none';
        // trigger hero reveal after preloader
        document.querySelectorAll('.hero .reveal').forEach(function (el) {
          el.classList.add('visible');
        });
      }, 500);
    }, 1200);
  });

  /* ============ NAVBAR SCROLL SHRINK ============ */
  var navbar = document.getElementById('navbar');

  function handleNavbarScroll() {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll();

  /* ============ SMOOTH SCROLL ============ */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href').slice(1);
      var target = document.getElementById(targetId);
      if (!target) return;
      e.preventDefault();

      var navHeight = navbar ? navbar.offsetHeight : 0;
      var targetTop = target.getBoundingClientRect().top + window.scrollY - navHeight - 8;

      window.scrollTo({ top: targetTop, behavior: 'smooth' });

      // close mobile menu if open
      closeMobileMenu();
    });
  });

  /* ============ HAMBURGER MOBILE MENU ============ */
  var hamburger = document.getElementById('hamburger');
  var navLinks = document.getElementById('navLinks');

  function closeMobileMenu() {
    if (hamburger && navLinks) {
      hamburger.classList.remove('open');
      navLinks.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }
  }

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      var isOpen = navLinks.classList.toggle('open');
      hamburger.classList.toggle('open', isOpen);
      hamburger.setAttribute('aria-expanded', String(isOpen));
      document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    // close on escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMobileMenu();
    });
  }

  /* ============ ACTIVE NAV TRACKING ============ */
  var sections = document.querySelectorAll('section[id]');
  var navLinkEls = document.querySelectorAll('.nav-link[data-section]');

  function updateActiveNav() {
    var scrollY = window.scrollY;
    var navH = navbar ? navbar.offsetHeight : 0;
    var current = '';

    sections.forEach(function (section) {
      var sectionTop = section.offsetTop - navH - 60;
      var sectionBottom = sectionTop + section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionBottom) {
        current = section.getAttribute('id');
      }
    });

    navLinkEls.forEach(function (link) {
      link.classList.toggle('active', link.dataset.section === current);
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });
  updateActiveNav();

  /* ============ SCROLL REVEAL ============ */
  var revealEls = document.querySelectorAll('.reveal');

  var revealObserver = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  revealEls.forEach(function (el) {
    revealObserver.observe(el);
  });

  /* ============ ANIMATED COUNTERS ============ */
  var counters = document.querySelectorAll('.stat-number[data-target]');
  var countersAnimated = false;

  function easeOut(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function animateCounter(el) {
    var target = parseInt(el.dataset.target, 10);
    var suffix = el.dataset.suffix || '';
    var duration = 1600;
    var start = null;

    function step(timestamp) {
      if (!start) start = timestamp;
      var elapsed = timestamp - start;
      var progress = Math.min(elapsed / duration, 1);
      var current = Math.floor(easeOut(progress) * target);
      el.textContent = current + suffix;
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target + suffix;
      }
    }

    requestAnimationFrame(step);
  }

  var statsSection = document.querySelector('.stats-grid');

  if (statsSection) {
    var statsObserver = new IntersectionObserver(
      function (entries) {
        if (entries[0].isIntersecting && !countersAnimated) {
          countersAnimated = true;
          counters.forEach(function (counter, i) {
            setTimeout(function () { animateCounter(counter); }, i * 120);
          });
          statsObserver.disconnect();
        }
      },
      { threshold: 0.4 }
    );
    statsObserver.observe(statsSection);
  }

  /* ============ BACK TO TOP ============ */
  var backToTop = document.getElementById('backToTop');

  if (backToTop) {
    window.addEventListener('scroll', function () {
      backToTop.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ============ FOOTER YEAR ============ */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* ============ CONTACT FORM VALIDATION ============ */
  var form = document.getElementById('contactForm');
  var formSuccess = document.getElementById('formSuccess');

  function getField(id) { return document.getElementById(id); }
  function getError(id) { return document.getElementById(id + 'Error'); }

  function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function setError(fieldId, msg) {
    var field = getField(fieldId);
    var error = getError(fieldId);
    if (field) field.classList.toggle('error', !!msg);
    if (error) error.textContent = msg || '';
    return !!msg;
  }

  function validateForm() {
    var hasError = false;

    var name = getField('name');
    if (!name || !name.value.trim()) {
      hasError = setError('name', 'Please enter your name.') || hasError;
    } else {
      setError('name', '');
    }

    var email = getField('email');
    if (!email || !email.value.trim()) {
      hasError = setError('email', 'Please enter your email address.') || hasError;
    } else if (!validateEmail(email.value.trim())) {
      hasError = setError('email', 'Please enter a valid email address.') || hasError;
    } else {
      setError('email', '');
    }

    var business = getField('business');
    if (!business || !business.value.trim()) {
      hasError = setError('business', 'Please enter your business name.') || hasError;
    } else {
      setError('business', '');
    }

    var message = getField('message');
    if (!message || !message.value.trim()) {
      hasError = setError('message', 'Please tell us about your goals.') || hasError;
    } else {
      setError('message', '');
    }

    return !hasError;
  }

  if (form) {
    // live validation on blur
    ['name', 'email', 'business', 'message'].forEach(function (id) {
      var field = getField(id);
      if (field) {
        field.addEventListener('blur', validateForm);
        field.addEventListener('input', function () {
          if (field.classList.contains('error')) validateForm();
        });
      }
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validateForm()) return;

      // Simulate submission
      var submitBtn = form.querySelector('.btn--submit');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.querySelector('.btn-text').textContent = 'Sending…';
      }

      setTimeout(function () {
        form.style.display = 'none';
        if (formSuccess) {
          formSuccess.hidden = false;
          formSuccess.style.display = 'block';
          formSuccess.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }, 1000);
    });
  }

  /* ============ PARALLAX HERO ORBS ============ */
  var orb1 = document.querySelector('.hero-orb--1');
  var orb2 = document.querySelector('.hero-orb--2');

  if (orb1 && orb2) {
    window.addEventListener('mousemove', function (e) {
      var x = (e.clientX / window.innerWidth - 0.5) * 20;
      var y = (e.clientY / window.innerHeight - 0.5) * 20;

      orb1.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
      orb2.style.transform = 'translate(' + (-x * 0.5) + 'px, ' + (-y * 0.5) + 'px)';
    }, { passive: true });
  }

  /* ============ HERO MAPS RANK ANIMATION ============ */
  // subtle rank badge number cycling to show "before/after" effect
  var rankBadge = document.querySelector('.rank-badge--gold');
  if (rankBadge) {
    var positions = ['4', '3', '2', '1'];
    var posIdx = 0;
    var cycleInterval = setInterval(function () {
      posIdx++;
      if (posIdx < positions.length) {
        rankBadge.textContent = positions[posIdx];
        if (posIdx === positions.length - 1) {
          clearInterval(cycleInterval);
        }
      }
    }, 900);
  }

})();
