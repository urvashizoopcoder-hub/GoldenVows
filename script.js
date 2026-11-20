/* Royal Palace — live wedding invitation runtime (Just For You, JFY-WED-ROYAL-PALACE)
 * Data: window.JFY_DATA (assets/sample-data.js) | URL #data=<base64 JSON> | postMessage {type:'jfy:data',data}
 * Tokens: {{key}} or {{key|filter}}  filters: long, short, time, dm, initial
 * data-optional="key[,key2]" hides an element when all listed keys are empty.  data-fit="minPx" shrinks to fit.
 */
(window.JFY_READY || Promise.resolve()).then(function () {
  'use strict';
  var D = Object.assign({}, window.JFY_DATA || {});
  var Q = new URLSearchParams(location.search);
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var DAYS = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  var MON = ['January','February','March','April','May','June','July','August','September','October','November','December'];

  function pd(v) { var m = /^(\d{4})-(\d{2})-(\d{2})(?:T(\d{1,2}):(\d{2}))?/.exec(String(v || '')); if (!m) return null; return { y:+m[1], mo:+m[2]-1, d:+m[3], h: m[4]==null?null:+m[4], mi: m[5]==null?0:+m[5] }; }
  function ord(n) { var s=['th','st','nd','rd'], v=n%100; return n+(s[(v-20)%10]||s[v]||s[0]); }
  function dow(p) { return new Date(Date.UTC(p.y,p.mo,p.d)).getUTCDay(); }
  function fmt(val, f) {
    if (val == null) return '';
    if (!f) return String(val);
    if (f === 'initial') return String(val).trim().charAt(0).toUpperCase();
    var p = pd(val); if (!p) return String(val);
    if (f === 'long') return DAYS[dow(p)] + ' | ' + ord(p.d) + ' ' + MON[p.mo].slice(0,3) + ' ' + p.y;
    if (f === 'short') return DAYS[dow(p)].slice(0,3) + ', ' + p.d + ' ' + MON[p.mo].slice(0,3) + ' ' + p.y;
    if (f === 'dm') return ord(p.d) + ' ' + MON[p.mo] + ' ' + p.y;
    if (f === 'time') { if (p.h == null) return ''; var h = p.h % 12 || 12; return h + ':' + String(p.mi).padStart(2,'0') + (p.h < 12 ? ' AM' : ' PM'); }
    return String(val);
  }
  var TOK = /\{\{\s*([\w.]+)\s*(?:\|\s*(\w+)\s*)?\}\}/g;
  function interp(str, ctx) { return String(str).replace(TOK, function (_, k, f) { var v = ctx[k]; return (v == null || (typeof v === 'object')) ? (Array.isArray(v) ? '' : '') : fmt(v, f); }); }
  function empty(ctx, k) { var v = ctx[k]; return v == null || (Array.isArray(v) ? v.length === 0 : String(v).trim() === ''); }
  function bind(root, ctx) {
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null), n, list = [];
    while ((n = w.nextNode())) if (n.nodeValue.indexOf('{{') > -1) list.push(n);
    list.forEach(function (t) { t.nodeValue = interp(t.nodeValue, ctx); });
    var els = root.querySelectorAll ? root.querySelectorAll('*') : [];
    Array.prototype.forEach.call(els, function (el) {
      Array.prototype.slice.call(el.attributes).forEach(function (a) { if (a.value.indexOf('{{') > -1) el.setAttribute(a.name, interp(a.value, ctx)); });
    });
    Array.prototype.forEach.call(root.querySelectorAll('[data-optional]'), function (el) {
      var ks = el.getAttribute('data-optional').split(',').map(function (s) { return s.trim(); });
      el.classList.toggle('is-empty', ks.every(function (k) { return empty(ctx, k); }));
    });
  }
  // Google Calendar link (times are IST)
  function calUrl(title, iso, venue, details) {
    var p = pd(iso); if (!p) return '#';
    var h = p.h == null ? 10 : p.h;
    var start = new Date(Date.UTC(p.y, p.mo, p.d, h, p.mi) - 330 * 60000), end = new Date(start.getTime() + 3 * 3600000);
    var z = function (d) { return d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, ''); };
    return 'https://calendar.google.com/calendar/render?action=TEMPLATE&text=' + encodeURIComponent(title) + '&dates=' + z(start) + '/' + z(end) + '&location=' + encodeURIComponent(venue || '') + '&details=' + encodeURIComponent(details || '') + '&ctz=Asia/Kolkata';
  }
  function mapUrl(q) { return 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(q || ''); }
  var couple = D.bride_name ? ((D.groom_name || '') + ' & ' + D.bride_name) : (D.groom_name || '');
  var fullCelebrants = D.bride_full_name ? ((D.groom_full_name || '') + ' & ' + D.bride_full_name) : (D.groom_full_name || '');
  var events = (Array.isArray(D.events) ? D.events : []).filter(function (e) { return e && e.name; });

  /* ---------- render ---------- */
  function render() {
    document.title = interp(document.title, D);
    bind(document.body, D);
    $$('[data-src]').forEach(function (el) { var v = el.getAttribute('data-src'); if (v && v.indexOf('{{') < 0) el.src = v; });
    $$('[data-bg]').forEach(function (el) { var v = el.getAttribute('data-bg'); if (v) el.style.backgroundImage = 'url("' + v + '")'; });
    $$('[data-fit]').forEach(fit);
    var calSuffix = D.cal_suffix || ' — Invitation';
    var main = calUrl(couple + calSuffix, D.event_date, D.venue, (D.occasion_title || 'Celebration') + ' of ' + fullCelebrants);
    $('#remindBtn').href = main; $('#stdCal').href = main;
    var wa = String(D.rsvp_whatsapp || '').replace(/\D/g, '');
    var waText = D.rsvp_default_msg || ('Congratulations ' + couple + '! 💐 Looking forward to celebrating with you.');
    $('#msgBtn').href = wa ? 'https://wa.me/' + wa + '?text=' + encodeURIComponent(waText) : '#rsvp';
    if (!wa) $('#msgBtn').removeAttribute('target');
    $('#mapFrame').src = 'https://maps.google.com/maps?q=' + encodeURIComponent((D.venue || '') + ' ' + (D.venue_address || '')) + '&z=14&output=embed';
    buildCalendar(); buildEvents(); buildGallery(); buildChecks();
  }
  function fit(el) {
    var min = parseFloat(el.getAttribute('data-fit')) || 14;
    el.style.fontSize = ''; var fs = parseFloat(getComputedStyle(el).fontSize);
    var box = el.parentElement.clientWidth - 2;
    var guard = 40;
    while (el.scrollWidth > box && fs > min && guard--) { fs -= 1; el.style.fontSize = fs + 'px'; }
    if (el.scrollWidth > box) { el.style.whiteSpace = 'normal'; el.style.lineHeight = '1.15'; }
  }

  function buildCalendar() {
    var p = pd(D.event_date); if (!p) { $('#std').classList.add('is-empty'); return; }
    $('#calMonth').innerHTML = '<span class="cal__acc">' + p.d + '</span> ' + MON[p.mo].toUpperCase() + ' ' + p.y;
    $('#calDay').textContent = p.d;
    var g = $('#calGrid'), html = '';
    'SMTWTFS'.split('').forEach(function (c) { html += '<span class="wd">' + c + '</span>'; });
    var first = new Date(Date.UTC(p.y, p.mo, 1)).getUTCDay(), days = new Date(Date.UTC(p.y, p.mo + 1, 0)).getUTCDate();
    var evDays = {}; events.forEach(function (e) { var q = pd(e.date); if (q && q.y === p.y && q.mo === p.mo) evDays[q.d] = 1; });
    for (var i = 0; i < first; i++) html += '<span></span>';
    for (var d = 1; d <= days; d++) html += '<span class="d' + (d === p.d ? ' main' : evDays[d] ? ' ev' : '') + '"><b>' + d + '</b></span>';
    g.innerHTML = html;
  }

  function buildEvents() {
    var sec = $('#events');
    if (!events.length) { sec.classList.add('is-empty'); return; }
    sec.style.setProperty('--n', events.length);
    var tpl = $('#evTpl').innerHTML, cards = $('#evCards'), imgs = $('#evImgs'), dots = $('#evDots');
    events.forEach(function (e, i) {
      var ctx = Object.assign({}, e);
      ctx.venue = e.venue || D.venue || '';
      ctx.map_url = e.map_url || mapUrl(ctx.venue);
      ctx.cal_url = calUrl(e.name + ' — ' + couple, e.date, ctx.venue, e.note || '');
      var p = pd(e.date); ctx.time = p && p.h != null ? 'y' : '';
      var wrap = document.createElement('div'); wrap.innerHTML = tpl; var card = wrap.firstElementChild;
      bind(wrap, ctx); cards.appendChild(card);
      var im = new Image(); im.alt = e.name; im.decoding = 'async'; if (i > 1) im.loading = 'lazy'; im.src = e.image || D.hero_image; imgs.appendChild(im);
      dots.appendChild(document.createElement('i'));
    });
    setEvent(0);
  }
  var curEv = -1;
  function setEvent(i) {
    if (i === curEv) return; curEv = i;
    $$('#evCards .evcard').forEach(function (c, k) { c.classList.toggle('on', k === i); });
    $$('#evImgs img').forEach(function (c, k) { c.classList.toggle('on', k === i); });
    $$('#evDots i').forEach(function (c, k) { c.classList.toggle('on', k === i); });
  }
  function onScrollEvents() {
    var sec = $('#events'); if (!events.length) return;
    var r = sec.getBoundingClientRect(), span = sec.offsetHeight - innerHeight;
    var prog = Math.min(1, Math.max(0, -r.top / Math.max(1, span)));
    setEvent(Math.min(events.length - 1, Math.floor(prog * events.length * 0.999)));
  }

  /* ---------- gallery ring ---------- */
  var ringAngle = 0, ringStep = 60;
  function buildGallery() {
    var g = (D.gallery || []).filter(Boolean), ring = $('#ring');
    if (!g.length) return;
    ringStep = 360 / g.length;
    var r = Math.round(150 / 2 / Math.tan(Math.PI / g.length)) + 34;
    g.forEach(function (src, i) {
      var it = document.createElement('div'); it.className = 'ring__item';
      it.style.transform = 'rotateY(' + (i * ringStep) + 'deg) translateZ(' + r + 'px)';
      it.innerHTML = '<img loading="lazy" alt="Photo ' + (i + 1) + '" src="' + src + '">';
      it.addEventListener('click', function () { if (!dragMoved) openLb(src); });
      ring.appendChild(it);
    });
    ring.style.transform = 'translateZ(-' + r + 'px) rotateY(0deg)';
    ring.dataset.r = r;
    var wrap = $('#ringWrap'), sx = 0, sa = 0, down = false, dragMoved = false;
    function setA(a) { ringAngle = a; ring.style.transform = 'translateZ(-' + r + 'px) rotateY(' + a + 'deg)'; }
    wrap.addEventListener('pointerdown', function (e) { down = true; dragMoved = false; sx = e.clientX; sa = ringAngle; ring.classList.add('is-drag'); });
    window.addEventListener('pointermove', function (e) { if (!down) return; var dx = e.clientX - sx; if (Math.abs(dx) > 4) dragMoved = true; setA(sa + dx * 0.45); });
    window.addEventListener('pointerup', function () { if (!down) return; down = false; ring.classList.remove('is-drag'); setA(Math.round(ringAngle / ringStep) * ringStep); setTimeout(function () { dragMoved = false; }, 50); });
    $('#ringPrev').onclick = function () { setA(ringAngle + ringStep); };
    $('#ringNext').onclick = function () { setA(ringAngle - ringStep); };
    window.JFYRoyal.spin = function () { setA(ringAngle - ringStep); };
  }
  function openLb(src) { var lb = $('#lightbox'); $('img', lb).src = src; lb.hidden = false; }
  $('#lightbox').addEventListener('click', function () { this.hidden = true; });

  /* ---------- countdown ---------- */
  function tick() {
    var p = pd(D.event_date); if (!p) return;
    var t = Date.UTC(p.y, p.mo, p.d, p.h == null ? 0 : p.h, p.mi) - 330 * 60000 - Date.now();
    if (t <= 0) { $('#countdown').hidden = true; $('#cdDone').hidden = false; return; }
    var s = Math.floor(t / 1000), pad = function (n) { return String(n).padStart(2, '0'); };
    $('#cdD').textContent = pad(Math.floor(s / 86400)); $('#cdH').textContent = pad(Math.floor(s % 86400 / 3600));
    $('#cdM').textContent = pad(Math.floor(s % 3600 / 60)); $('#cdS').textContent = pad(s % 60);
  }

  /* ---------- envelope ---------- */
  function openEnvelope() {
    var std = $('#std'); if (std.classList.contains('is-open')) return;
    var env = $('#env'), cal = $('#envCard .cal'), ch = Math.ceil(cal.scrollHeight) + 2, eh = env.offsetHeight;
    env.style.setProperty('--cardH', ch + 'px'); env.style.setProperty('--cardTop', Math.round((eh - ch) / 2) + 'px'); std.style.setProperty('--stageH', (ch + 24) + 'px');
    std.classList.add('is-open'); $('#envHint').textContent = 'Mark your calendar ❤';
    var r = $('#env').getBoundingClientRect(); burst(r.left + r.width / 2, r.top + r.height / 2, 26);
  }
  $('#env').addEventListener('click', openEnvelope);
  $('#env').addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openEnvelope(); } });

  /* ---------- RSVP ---------- */
  var guests = 1;
  function buildChecks() {
    var box = $('#evChecks');
    if (!events.length) { $('#fEvents').classList.add('is-empty'); return; }
    box.innerHTML = events.map(function (e, i) { return '<label><input type="checkbox" name="ev" value="' + esc(e.name) + '" checked><span>' + esc(e.name) + '</span></label>'; }).join('');
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var form = $('#rsvpForm');
  form.addEventListener('change', function () { form.classList.toggle('is-no', form.attending.value === 'no'); });
  $('#gMinus').onclick = function () { guests = Math.max(1, guests - 1); $('#gCount').textContent = guests; };
  $('#gPlus').onclick = function () { guests = Math.min(20, guests + 1); $('#gCount').textContent = guests; };
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name = form.name.value.trim();
    if (!name) { $('#rErr').hidden = false; form.name.focus(); return; }
    $('#rErr').hidden = true;
    var yes = form.attending.value === 'yes';
    var evs = $$('#evChecks input:checked').map(function (c) { return c.value; });
    var phone = form.phone.value.replace(/\D/g, '');
    var r = { name: name, attending: yes, guests: yes ? guests : 0, events: yes ? evs : [], phone: phone ? form.cc.value + ' ' + phone : '', note: form.note.value.trim(), at: new Date().toISOString() };
    try { localStorage.setItem('jfy-royal-rsvp', JSON.stringify(r)); } catch (_) {}
    try { (window.parent !== window) && window.parent.postMessage({ type: 'jfy:rsvp', data: r }, '*'); } catch (_) {}
    if (window.JFYBridge && JFYBridge.onRsvp) try { JFYBridge.onRsvp(JSON.stringify(r)); } catch (_) {}
    if (D.rsvp_endpoint) fetch(D.rsvp_endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(r) }).catch(function () {});
    var occTitle = D.occasion_title || 'celebration';
    var msg = yes
      ? 'Namaste! This is ' + name + '. Joyfully confirming ' + guests + ' guest' + (guests > 1 ? 's' : '') + ' for ' + (evs.length ? evs.join(', ') : occTitle) + ' of ' + couple + '. 💐'
      : 'Namaste! This is ' + name + '. With regret, I won\'t be able to attend, but sending all my blessings and best wishes to ' + couple + '. 💐';
    if (r.note) msg += '\n\n“' + r.note + '”';
    $('#thanksMsg').textContent = yes
      ? 'Dear ' + name + ', we can\'t wait to celebrate with you' + (evs.length ? ' at the ' + evs.join(', ') : '') + '. ' + guests + ' guest' + (guests > 1 ? 's' : '') + ' noted.'
      : 'Dear ' + name + ', we\'ll miss you! Thank you for your love and blessings.';
    var wa = String(D.rsvp_whatsapp || '').replace(/\D/g, '');
    var b = $('#waBtn'); if (wa) { b.href = 'https://wa.me/' + wa + '?text=' + encodeURIComponent(msg); b.hidden = false; } else b.hidden = true;
    form.hidden = true; $('#thanks').hidden = false;
    var rc = $('#thanks').getBoundingClientRect(); burst(rc.left + rc.width / 2, rc.top + 40, 30);
  });
  $('#editRsvp').onclick = function () { $('#thanks').hidden = true; form.hidden = false; };

  /* ---------- music ---------- */
  var audio = $('#music'), mBtn = $('#musicBtn'), musicOn = Q.get('music') !== '0' && D.music_enabled !== false;
  function playMusic() { if (!musicOn || !audio.src) return; audio.volume = 0; var p = audio.play(); if (p && p.catch) p.catch(function () {}); fadeTo(0.85); mBtn.classList.remove('is-off'); }
  function fadeTo(v) { var s = audio.volume, t0 = performance.now(); (function f(t) { var k = Math.min(1, (t - t0) / 1200); audio.volume = Math.max(0, Math.min(1, s + (v - s) * k)); if (k < 1) requestAnimationFrame(f); })(t0); }
  mBtn.onclick = function () { if (audio.paused) { musicOn = true; playMusic(); } else { audio.pause(); mBtn.classList.add('is-off'); } };
  document.addEventListener('visibilitychange', function () { if (document.hidden && !audio.paused) { audio.pause(); audio.__resume = true; } else if (!document.hidden && audio.__resume) { audio.__resume = false; audio.play().catch(function () {}); } });

  /* ---------- answer the call (slider) ---------- */
  var slider = $('#slider'), knob = $('#knob'), dragging = false, sx0 = 0, prog = 0, opened = false;
  function track() { slider.style.setProperty('--track', (slider.clientWidth - 14) + 'px'); }
  function setP(p) { prog = Math.max(0, Math.min(1, p)); slider.style.setProperty('--p', prog); }
  knob.addEventListener('pointerdown', function (e) { dragging = true; sx0 = e.clientX; track(); slider.classList.add('is-drag'); slider.classList.remove('is-back'); knob.setPointerCapture && knob.setPointerCapture(e.pointerId); });
  knob.addEventListener('pointermove', function (e) { if (!dragging) return; var max = slider.clientWidth - 14 - knob.offsetWidth; setP((e.clientX - sx0) / max); });
  function release(e) {
    if (!dragging) return; dragging = false; slider.classList.remove('is-drag');
    var moved = Math.abs(e.clientX - sx0);
    if (prog > 0.7 || moved < 6) { answer(); } else { slider.classList.add('is-back'); setP(0); }
  }
  knob.addEventListener('pointerup', release); knob.addEventListener('pointercancel', release);
  function answer() {
    if (opened) return; opened = true; track(); slider.classList.add('is-back', 'is-done'); setP(1);
    playMusic();
    setTimeout(function () {
      $('#call').classList.add('is-answered');
      document.body.classList.remove('is-locked'); document.body.classList.add('is-open');
      window.scrollTo(0, 0);
      burst(innerWidth / 2, innerHeight * 0.4, 40);
      petals.boost(60);
      setTimeout(function () { $('#call').hidden = true; }, 1300);
    }, 450);
  }

  /* ---------- tap to feel the magic: sparkles + tilt parallax ---------- */
  function burst(x, y, n) {
    for (var i = 0; i < n; i++) {
      var s = document.createElement('i'); s.className = 'spark';
      var a = Math.random() * Math.PI * 2, d = 60 + Math.random() * 140;
      s.style.left = x + 'px'; s.style.top = y + 'px';
      s.style.setProperty('--x', Math.cos(a) * d + 'px'); s.style.setProperty('--y', Math.sin(a) * d + 'px');
      s.style.animationDuration = (0.8 + Math.random() * 0.8) + 's';
      document.body.appendChild(s); setTimeout(s.remove.bind(s), 1700);
    }
  }
  var tilt = { x: 0, y: 0 };
  function enableTilt() {
    var go = function () { window.addEventListener('deviceorientation', function (e) { tilt.x = Math.max(-1, Math.min(1, (e.gamma || 0) / 30)); tilt.y = Math.max(-1, Math.min(1, ((e.beta || 0) - 45) / 30)); }); };
    if (window.DeviceOrientationEvent && typeof DeviceOrientationEvent.requestPermission === 'function') DeviceOrientationEvent.requestPermission().then(function (s) { if (s === 'granted') go(); }).catch(function () {}); else go();
  }
  window.addEventListener('pointermove', function (e) { if (e.pointerType === 'mouse') { tilt.x = (e.clientX / innerWidth - .5) * 2; tilt.y = (e.clientY / innerHeight - .5) * 2; } });
  $$('[data-magic]').forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); enableTilt(); var r = b.getBoundingClientRect(); burst(r.left + r.width / 2, r.top + r.height / 2, 36); petals.boost(50); if (b.closest('.call')) { /* magic on the call screen also plays music preview */ playMusic(); } }); });

  /* ---------- falling petals (canvas) ---------- */
  var petals = (function () {
    var c = $('#petals'), x = c.getContext('2d'), P = [], W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1), extra = 0;
    var cols = ['#f4a7b5', '#ee8fa3', '#f9c5cf', '#e77d93', '#fbd9de'];
    function size() { W = c.clientWidth; H = c.clientHeight; c.width = W * dpr; c.height = H * dpr; x.setTransform(dpr, 0, 0, dpr, 0, 0); }
    function mk(top) { return { x: Math.random() * W, y: top ? -20 - Math.random() * H * 0.3 : Math.random() * H, r: 5 + Math.random() * 7, vy: 0.5 + Math.random() * 1.1, vx: -0.3 + Math.random() * 0.6, a: Math.random() * 6.28, va: -0.03 + Math.random() * 0.06, sw: Math.random() * 6.28, c: cols[(Math.random() * cols.length) | 0] }; }
    function draw(p) { x.save(); x.translate(p.x, p.y); x.rotate(p.a); x.scale(1, 0.6 + 0.4 * Math.sin(p.sw)); x.fillStyle = p.c; x.globalAlpha = 0.85; x.beginPath(); x.moveTo(0, -p.r); x.bezierCurveTo(p.r, -p.r, p.r, p.r * 0.6, 0, p.r); x.bezierCurveTo(-p.r, p.r * 0.6, -p.r, -p.r, 0, -p.r); x.fill(); x.restore(); }
    function loop() {
      x.clearRect(0, 0, W, H);
      var want = (document.body.classList.contains('is-open') ? 11 : 0) + Math.round(extra);
      while (P.length < want) P.push(mk(true));
      for (var i = P.length - 1; i >= 0; i--) { var p = P[i]; p.y += p.vy; p.sw += 0.04; p.x += p.vx + Math.sin(p.sw) * 0.6; p.a += p.va; if (p.y > H + 20) { if (P.length > want) P.splice(i, 1); else Object.assign(p, mk(true)); } else draw(p); }
      if (extra > 0) extra = Math.max(0, extra - 0.25);
      requestAnimationFrame(loop);
    }
    window.addEventListener('resize', size); size(); requestAnimationFrame(loop);
    return { boost: function (n) { extra += n; } };
  })();

  /* ---------- sky lanterns ---------- */
  (function () {
    var box = $('#lanterns'), html = '';
    for (var i = 0; i < 9; i++) html += '<svg class="lantern" viewBox="0 0 40 56" style="left:' + (4 + Math.random() * 88) + '%;--s:' + (22 + Math.random() * 26) + 'px;--d:' + (20 + Math.random() * 16) + 's;--delay:' + (-Math.random() * 30) + 's;--dx:' + (-40 + Math.random() * 80) + 'px"><use href="#lantern"/></svg>';
    box.innerHTML = html;
  })();

  /* ---------- scroll: reveal, parallax, pinned events ---------- */
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
  var parEls = [], ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      ticking = false; var y = scrollY;
      parEls.forEach(function (el) { el.style.transform = 'translate3d(' + (tilt.x * -8) + 'px,' + (y * el.__k) + 'px,0)'; });
      onScrollEvents();
    });
  }

  /* ---------- clock + loader ---------- */
  function clock() { var d = new Date(), h = d.getHours() % 12 || 12; $('#callClock').textContent = h + ':' + String(d.getMinutes()).padStart(2, '0'); }

  function boot() {
    render(); track(); clock(); setInterval(clock, 15000); tick(); setInterval(tick, 1000);
    $$('.reveal').forEach(function (el) { io.observe(el); });
    parEls = $$('[data-par]'); parEls.forEach(function (el) { el.__k = parseFloat(el.getAttribute('data-par')) || 0; });
    window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('resize', function () { $$('[data-fit]').forEach(fit); track(); onScroll(); });
    (function tiltLoop() { var bg = $('.call__bg'); if (bg && !opened) bg.style.translate = (tilt.x * -12) + 'px ' + (tilt.y * -8) + 'px'; requestAnimationFrame(tiltLoop); })();
    // loader progress on key images
    var srcs = [D.cover_image, D.hero_image].filter(Boolean), done = 0, pct = 0, shown = 0;
    var finish = function () { $('#loaderPct').textContent = '100'; setTimeout(function () { $('#loader').classList.add('is-done'); if (Q.get('autoplay') === '1') setTimeout(answer, 1200); }, 250); };
    var anim = setInterval(function () { shown += (Math.max(pct, shown + 1) - shown) * 0.25; $('#loaderPct').textContent = Math.min(99, Math.round(shown)); }, 60);
    if (!srcs.length) { clearInterval(anim); finish(); }
    srcs.forEach(function (s) { var im = new Image(); im.onload = im.onerror = function () { done++; pct = done / srcs.length * 100; if (done === srcs.length) setTimeout(function () { clearInterval(anim); finish(); }, 350); }; im.src = s; });
    setTimeout(function () { if (!$('#loader').classList.contains('is-done')) { clearInterval(anim); finish(); } }, 6000);
    if (Q.get('skip') === '1') { setTimeout(answer, 100); }
    if (Q.get('preview') === '1') { $('#loader').classList.add('is-done'); var sy = +Q.get('y') || 0; if (sy) setTimeout(function () { window.scrollTo(0, sy); }, 700); }
  }
  window.JFYRoyal = { answer: function () { answer(); }, openEnvelope: openEnvelope, data: D, spin: function () {} };
  window.addEventListener('message', function (e) { var m = e.data || {}; if (m.type === 'jfy:data' && m.data && window.JFYCodec) { JFYCodec.encode(m.data).then(function (s) { location.hash = 'data=' + s; location.reload(); }); } });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();

});
