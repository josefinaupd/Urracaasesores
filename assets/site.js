// Menú móvil, desplegable "Urraca Abogados", cabecera y animaciones de entrada
(function () {
  var body = document.body;
  var burger = document.querySelector('.burger');
  var header = document.querySelector('header.site');

  burger.addEventListener('click', function () {
    var open = body.classList.toggle('menu-open');
    burger.setAttribute('aria-expanded', open);
  });

  document.querySelectorAll('.has-sub > button').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = btn.parentElement.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  });

  function closeSubs(except) {
    document.querySelectorAll('.has-sub.open').forEach(function (li) {
      if (li === except) return;
      li.classList.remove('open');
      li.firstElementChild.setAttribute('aria-expanded', false);
    });
  }
  document.addEventListener('click', function (e) { closeSubs(e.target.closest('.has-sub')); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    closeSubs(null);
    if (body.classList.contains('menu-open')) { body.classList.remove('menu-open'); burger.setAttribute('aria-expanded', false); }
  });

  // En móvil el submenú de la página actual aparece abierto
  if (window.matchMedia('(max-width: 860px)').matches) {
    var active = document.querySelector('.has-sub.active');
    if (active) { active.classList.add('open'); active.firstElementChild.setAttribute('aria-expanded', true); }
  }

  function onScroll() { header.classList.toggle('scrolled', window.scrollY > 4); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if ('IntersectionObserver' in window) {
    var els = document.querySelectorAll('.home-block .wrap > *, .tile, .svc, .main > *, .areas, .cta .wrap, .contact .wrap > *');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { el.classList.add('reveal'); io.observe(el); });
  }
})();
