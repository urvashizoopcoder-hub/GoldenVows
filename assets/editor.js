/* Royal Palace invitation editor — fills the form, shows a live preview, and builds a shareable link (#data=...). */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var SAMPLE = JSON.parse(JSON.stringify(window.JFY_DATA || {}));
  var TEXT = ['groom_name','groom_full_name','groom_parents','bride_name','bride_full_name','bride_parents','venue','venue_address','venue_map_url','invite_message','couple_quote','closing_quote','family_signoff','hashtag','rsvp_whatsapp','rsvp_deadline'];
  var PHOTOS = ['groom_photo','bride_photo','cover_image'];
  var form = $('#ed'), photos = {}, pvTimer = null, pvN = 0, DRAFT = 'jfy-royal-draft';

  function split(dt) { var m = /^(\d{4}-\d{2}-\d{2})(?:T(\d{2}:\d{2}))?/.exec(dt || ''); return m ? [m[1], m[2] || ''] : ['', '']; }

  /* ---------- fill form from data ---------- */
  function load(d) {
    TEXT.forEach(function (k) { if (form[k]) form[k].value = d[k] || ''; });
    var dt = split(d.event_date); form.event_date.value = dt[0]; form.event_time.value = d.event_time || dt[1];
    form.music_enabled.checked = d.music_enabled !== false; form.show_gallery.checked = d.show_gallery !== false;
    photos = {}; PHOTOS.forEach(function (k) { if (d[k] && /^data:/.test(d[k])) photos[k] = d[k]; });
    syncPhotos();
    $('#evList').innerHTML = ''; (d.events || []).forEach(addEvent); renumber();
  }
  function addEvent(e) {
    e = e || {};
    var node = $('#evTpl').content.firstElementChild.cloneNode(true), dt = split(e.date);
    $('[data-k=name]', node).value = e.name || ''; $('[data-k=date]', node).value = dt[0]; $('[data-k=time]', node).value = e.time || dt[1];
    $('[data-k=venue]', node).value = e.venue || ''; $('[data-k=map_url]', node).value = e.map_url || ''; $('[data-k=dress]', node).value = e.dress || '';
    $('.ev__del', node).onclick = function () { node.remove(); renumber(); schedule(); };
    $('#evList').appendChild(node); renumber();
    return node;
  }
  function renumber() { $$('#evList .ev').forEach(function (n, i) { $('.ev__no', n).textContent = 'Event ' + (i + 1); }); }

  /* ---------- read form into data ---------- */
  function collect() {
    var d = {};
    TEXT.forEach(function (k) { var v = (form[k].value || '').trim(); if (v) d[k] = v; });
    if (d.rsvp_whatsapp) d.rsvp_whatsapp = d.rsvp_whatsapp.replace(/\D/g, '');
    if (form.event_date.value) d.event_date = form.event_date.value + (form.event_time.value ? 'T' + form.event_time.value : '');
    if (!form.music_enabled.checked) d.music_enabled = false;
    if (!form.show_gallery.checked) d.show_gallery = false;
    PHOTOS.forEach(function (k) { if (photos[k]) d[k] = photos[k]; });
    d.events = $$('#evList .ev').map(function (n) {
      var g = function (k) { return ($('[data-k=' + k + ']', n).value || '').trim(); };
      var e = { name: g('name') }; if (!e.name) return null;
      if (g('date')) e.date = g('date') + (g('time') ? 'T' + g('time') : '');
      ['venue', 'map_url', 'dress'].forEach(function (k) { if (g(k)) e[k] = g(k); });
      return e;
    }).filter(Boolean);
    return d;
  }

  /* ---------- live preview ---------- */
  function schedule() { clearTimeout(pvTimer); pvTimer = setTimeout(preview, 650); }
  function preview() {
    var d = collect();
    try { localStorage.setItem(DRAFT, JSON.stringify(d)); } catch (e) { try { var lite = Object.assign({}, d); PHOTOS.forEach(function (k) { delete lite[k]; }); localStorage.setItem(DRAFT, JSON.stringify(lite)); } catch (_) {} }
    JFYCodec.encode(d).then(function (s) {
      var f = $('#pv'), y = 0; try { y = Math.round(f.contentWindow.scrollY || 0); } catch (_) {}
      f.src = 'index.html?skip=1&preview=1&music=0&y=' + y + '&r=' + (++pvN) + '#data=' + s;
    });
  }
  form.addEventListener('input', schedule);
  form.addEventListener('change', schedule);

  /* ---------- photos ---------- */
  function syncPhotos() {
    $$('[data-photo]').forEach(function (inp) {
      var k = inp.getAttribute('data-photo'), lab = inp.closest('.photo');
      lab.classList.toggle('has', !!photos[k]); $('.photo__btn', lab).textContent = photos[k] ? '✓ Photo added' : 'Upload';
      $('[data-clear=' + k + ']', lab).hidden = !photos[k];
    });
  }
  $$('[data-photo]').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var f = inp.files && inp.files[0]; if (!f) return;
      var k = inp.getAttribute('data-photo'), max = k === 'cover_image' ? 520 : 420;
      var img = new Image(), url = URL.createObjectURL(f);
      img.onload = function () {
        var s = Math.min(1, max / Math.max(img.width, img.height)), c = document.createElement('canvas');
        c.width = Math.round(img.width * s); c.height = Math.round(img.height * s);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        photos[k] = c.toDataURL('image/jpeg', 0.68); URL.revokeObjectURL(url); syncPhotos(); schedule();
      };
      img.onerror = function () { showErr('That file could not be read as an image.'); };
      img.src = url; inp.value = '';
    });
  });
  $$('[data-clear]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); delete photos[b.getAttribute('data-clear')]; syncPhotos(); schedule(); }); });

  /* ---------- events buttons ---------- */
  $('#evAdd').onclick = function () { var n = addEvent({}); $('input', n).focus(); schedule(); };
  $('#evPreset').onchange = function () { if (!this.value) return; addEvent({ name: this.value, date: form.event_date.value }); this.value = ''; schedule(); };
  $('#resetBtn').onclick = function () { load(SAMPLE); preview(); };
  $('#clearBtn').onclick = function () { load({ events: [], music_enabled: true }); preview(); };

  /* ---------- create & share ---------- */
  function showErr(t) { var e = $('#err'); e.textContent = t; e.hidden = !t; }
  $('#createBtn').onclick = function () {
    var d = collect(), miss = [];
    [['groom_name', "Groom's first name"], ['bride_name', "Bride's first name"], ['groom_full_name', "Groom's full name"], ['bride_full_name', "Bride's full name"], ['event_date', 'Wedding date'], ['venue', 'Venue']].forEach(function (p) { if (!d[p[0]]) miss.push(p[1]); });
    if (miss.length) { showErr('Please fill: ' + miss.join(', ')); document.body.classList.remove('v-preview'); var first = form.querySelector(':invalid'); if (first) { first.closest('details').open = true; first.focus(); } return; }
    showErr('');
    JFYCodec.encode(d).then(function (s) {
      var u = new URL('index.html', location.href); u.search = ''; u.hash = 'data=' + s;
      var link = u.toString(), msg = 'You are invited to the wedding of ' + d.groom_name + ' & ' + d.bride_name + ' 💐\nOpen your invitation: ' + link;
      $('#shareUrl').value = link; $('#openLink').href = link;
      $('#waShare').href = 'https://wa.me/?text=' + encodeURIComponent(msg);
      $('#lenNote').textContent = link.length > 6000 ? 'Your photos make this link long (' + Math.round(link.length / 1000) + 'k characters). It works in browsers, but if WhatsApp cuts it, remove the photos and share again.' : '';
      var ns = $('#nativeShare'); ns.hidden = !navigator.share; ns.onclick = function () { navigator.share({ title: 'Wedding invitation', text: msg.split('\n')[0], url: link }).catch(function () {}); };
      $('#sheet').hidden = false;
    });
  };
  $('#copyBtn').onclick = function () {
    var i = $('#shareUrl'), b = this; i.select();
    var ok = function () { b.textContent = 'Copied ✓'; setTimeout(function () { b.textContent = 'Copy'; }, 1800); };
    if (navigator.clipboard) navigator.clipboard.writeText(i.value).then(ok, function () { document.execCommand('copy'); ok(); }); else { document.execCommand('copy'); ok(); }
  };
  $('#sheetX').onclick = function () { $('#sheet').hidden = true; };

  /* ---------- tabs (mobile) ---------- */
  $$('.tab').forEach(function (t) { t.onclick = function () { $$('.tab').forEach(function (x) { x.classList.toggle('on', x === t); }); document.body.classList.toggle('v-preview', t.dataset.view === 'preview'); window.scrollTo(0, 0); }; });

  /* ---------- start: link data > saved draft > sample ---------- */
  var m = /[#&]data=([^&]+)/.exec(location.hash), start = Promise.resolve(null);
  if (m) start = JFYCodec.decode(m[1]).catch(function () { return null; });
  start.then(function (d) {
    if (!d) { try { d = JSON.parse(localStorage.getItem(DRAFT) || 'null'); } catch (_) { d = null; } }
    load(d || SAMPLE); preview();
  });
})();
