/* Conseil Camerounais de la Musique — scripts communs des pages intérieures */
(function () {
  'use strict';
  var EN = (window.CCM_LANGUE || document.documentElement.lang) === 'en';
  var reduit = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function fmt(v, d) { return d ? (EN ? v.toFixed(d) : v.toFixed(d).replace('.', ',')) : Math.round(v).toLocaleString(EN ? 'en-US' : 'fr-FR'); }

  /* Menu mobile */
  var mb = document.getElementById('menu-btn'), nav = document.getElementById('nav-principale');
  if (mb && nav) {
    mb.addEventListener('click', function () {
      var ouvert = nav.classList.toggle('ouvert');
      mb.setAttribute('aria-expanded', String(ouvert));
      mb.setAttribute('aria-label', EN ? (ouvert ? 'Close menu' : 'Open menu') : (ouvert ? 'Fermer le menu' : 'Ouvrir le menu'));
    });
  }

  /* Compteurs */
  var cs = Array.prototype.slice.call(document.querySelectorAll('[data-compte]'));
  function animer(el) {
    var cible = parseFloat(el.dataset.compte), dec = parseInt(el.dataset.dec, 10) || 0, t0 = null;
    function pas(t) {
      if (t0 === null) t0 = t;
      var x = Math.min(1, (t - t0) / 1600), e = 1 - Math.pow(1 - x, 3);
      el.textContent = fmt(cible * e, dec);
      if (x < 1) requestAnimationFrame(pas);
    }
    requestAnimationFrame(pas);
  }
  if (!reduit && 'IntersectionObserver' in window && cs.length) {
    cs.forEach(function (el) { el.textContent = fmt(0, parseInt(el.dataset.dec, 10) || 0); });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { animer(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.4 });
    cs.forEach(function (el) { io.observe(el); });
  }

  /* Lettre d'information : en attendant un service d'envoi */
  var form = document.getElementById('form-lettre');
  if (form) form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var c = document.getElementById('courriel');
    window.location.href = 'mailto:infos@ccm-cmc.org?subject=' + encodeURIComponent(EN ? 'Newsletter subscription' : "Inscription à la lettre d'information") + '&body=' + encodeURIComponent((EN ? 'Address: ' : 'Adresse : ') + (c ? c.value : ''));
  });
})();
