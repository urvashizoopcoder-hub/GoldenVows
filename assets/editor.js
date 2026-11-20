/* GoldenVows Celebration Studio — Comprehensive Multi-Occasion Editor & Dispatch Engine */
(function () {
  'use strict';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var PRESETS = window.OCCASION_PRESETS || {};
  var currentOccasion = 'wedding';
  var currentPalette = 'emerald-gold';
  var form = $('#ed');
  var photos = {};
  var pvTimer = null;
  var pvN = 0;
  var DRAFT_KEY = 'goldenvows_draft_v2';

  var TEXT_FIELDS = [
    'occasion_title', 'groom_name', 'groom_full_name', 'groom_parents',
    'bride_name', 'bride_full_name', 'bride_parents', 'venue',
    'venue_address', 'venue_map_url', 'invite_eyebrow', 'invite_message',
    'couple_quote', 'closing_quote', 'family_signoff', 'hashtag',
    'rsvp_whatsapp', 'rsvp_deadline', 'opening_style', 'view_mode', 'ambient_particles'
  ];
  var PHOTO_FIELDS = ['groom_photo', 'bride_photo', 'cover_image'];

  function splitDt(dt) {
    var m = /^(\d{4}-\d{2}-\d{2})(?:T(\d{2}:\d{2}))?/.exec(dt || '');
    return m ? [m[1], m[2] || ''] : ['', ''];
  }

  /* ---------- Switch Occasion Preset ---------- */
  function setOccasion(occName, skipFormFill) {
    currentOccasion = occName;
    var p = PRESETS[occName] || PRESETS.wedding;

    // Update occasion cards UI
    $$('.occasion-card').forEach(function (card) {
      card.classList.toggle('active', card.getAttribute('data-occ') === occName);
    });

    // Update dynamic field labels based on occasion
    if ($('#lblCel1')) $('#lblCel1').childNodes[0].nodeValue = (p.celebrant_1_label || "Celebrant 1") + ' *';
    if ($('#lblCel1Full')) $('#lblCel1Full').childNodes[0].nodeValue = (p.celebrant_1_full_label || "Celebrant 1 Full Name") + ' *';
    if ($('#lblCel1Par')) $('#lblCel1Par').childNodes[0].nodeValue = (p.celebrant_1_parents_label || "Blessing / Parents line") + ' ';
    if ($('#lblCel2')) $('#lblCel2').childNodes[0].nodeValue = (p.celebrant_2_label || "Celebrant 2") + ' *';
    if ($('#lblCel2Full')) $('#lblCel2Full').childNodes[0].nodeValue = (p.celebrant_2_full_label || "Celebrant 2 Full Name") + ' *';
    if ($('#lblCel2Par')) $('#lblCel2Par').childNodes[0].nodeValue = (p.celebrant_2_parents_label || "Blessing / Parents line") + ' ';

    // Update ceremony presets dropdown
    var sel = $('#evPreset');
    if (sel) {
      var opts = '<option value="">Quick add preset ceremony…</option>';
      (p.events || []).forEach(function (ev) {
        opts += '<option value="' + ev.name + '">' + ev.name + '</option>';
      });
      sel.innerHTML = opts;
    }

    if (!skipFormFill) {
      loadData(p);
    }
    schedulePreview();
  }

  /* ---------- Switch Color Theme Palette ---------- */
  function setPalette(palName) {
    currentPalette = palName;
    $$('.palette-card').forEach(function (card) {
      card.classList.toggle('active', card.getAttribute('data-pal') === palName);
    });
    schedulePreview();
  }

  /* ---------- Load Data Into Form ---------- */
  function loadData(d) {
    d = d || {};
    TEXT_FIELDS.forEach(function (k) {
      if (form[k]) form[k].value = d[k] || '';
    });

    var dt = splitDt(d.event_date);
    if (form.event_date) form.event_date.value = dt[0];
    if (form.event_time) form.event_time.value = d.event_time || dt[1];

    if (form.music_enabled) form.music_enabled.checked = d.music_enabled !== false;
    if (form.show_gallery) form.show_gallery.checked = d.show_gallery !== false;

    if (d.theme_palette) {
      currentPalette = d.theme_palette;
      $$('.palette-card').forEach(function (c) {
        c.classList.toggle('active', c.getAttribute('data-pal') === currentPalette);
      });
    }

    if (d.opening_style && form.opening_style) form.opening_style.value = d.opening_style;
    if (d.view_mode && form.view_mode) form.view_mode.value = d.view_mode;
    if (d.ambient_particles && form.ambient_particles) form.ambient_particles.value = d.ambient_particles;

    photos = {};
    PHOTO_FIELDS.forEach(function (k) {
      if (d[k] && /^data:/.test(d[k])) photos[k] = d[k];
    });
    syncPhotos();

    var evList = $('#evList');
    if (evList) {
      evList.innerHTML = '';
      (d.events || []).forEach(addEventRow);
      renumberEvents();
    }
  }

  /* ---------- Event Rows Management ---------- */
  function addEventRow(e) {
    e = e || {};
    var tpl = $('#evTpl');
    if (!tpl) return;
    var node = tpl.content.firstElementChild.cloneNode(true);
    var dt = splitDt(e.date);

    $('[data-k=name]', node).value = e.name || '';
    $('[data-k=date]', node).value = dt[0];
    $('[data-k=time]', node).value = e.time || dt[1];
    $('[data-k=venue]', node).value = e.venue || '';
    $('[data-k=map_url]', node).value = e.map_url || '';
    $('[data-k=dress]', node).value = e.dress || '';
    $('[data-k=note]', node).value = e.note || '';

    $('.ev__del', node).onclick = function () {
      node.remove();
      renumberEvents();
      schedulePreview();
    };

    $('#evList').appendChild(node);
    renumberEvents();
    return node;
  }

  function renumberEvents() {
    $$('#evList .ev').forEach(function (n, i) {
      var no = $('.ev__no', n);
      if (no) no.textContent = 'Ceremony ' + (i + 1);
    });
  }

  /* ---------- Collect Form Data ---------- */
  function collectData() {
    var d = {
      occasion_type: currentOccasion,
      theme_palette: currentPalette
    };

    TEXT_FIELDS.forEach(function (k) {
      if (form[k]) {
        var v = (form[k].value || '').trim();
        if (v) d[k] = v;
      }
    });

    if (d.rsvp_whatsapp) {
      d.rsvp_whatsapp = d.rsvp_whatsapp.replace(/\D/g, '');
    }

    if (form.event_date && form.event_date.value) {
      d.event_date = form.event_date.value + (form.event_time && form.event_time.value ? 'T' + form.event_time.value : '');
    }

    if (form.music_enabled) d.music_enabled = form.music_enabled.checked;
    if (form.show_gallery) d.show_gallery = form.show_gallery.checked;

    PHOTO_FIELDS.forEach(function (k) {
      if (photos[k]) d[k] = photos[k];
    });

    d.events = $$('#evList .ev').map(function (n) {
      var g = function (k) { return ($('[data-k=' + k + ']', n).value || '').trim(); };
      var ev = { name: g('name') };
      if (!ev.name) return null;
      if (g('date')) ev.date = g('date') + (g('time') ? 'T' + g('time') : '');
      ['venue', 'map_url', 'dress', 'note'].forEach(function (k) {
        if (g(k)) ev[k] = g(k);
      });
      return ev;
    }).filter(Boolean);

    return d;
  }

  /* ---------- Live Preview Scheduler ---------- */
  function schedulePreview() {
    clearTimeout(pvTimer);
    pvTimer = setTimeout(runPreview, 450);
  }

  function runPreview() {
    var d = collectData();
    try {
      localStorage.setItem(DRAFT_KEY, JSON.stringify(d));
    } catch (_) {}

    if (!window.JFYCodec) return;

    window.JFYCodec.encode(d).then(function (s) {
      var f = $('#pv');
      if (!f) return;
      var y = 0;
      try { y = Math.round(f.contentWindow.scrollY || 0); } catch (_) {}
      f.src = 'invite.html?skip=1&preview=1&music=0&y=' + y + '&r=' + (++pvN) + '#data=' + s;
    });
  }

  /* ---------- Photo Upload Helpers ---------- */
  function syncPhotos() {
    $$('[data-photo]').forEach(function (inp) {
      var k = inp.getAttribute('data-photo');
      var lab = inp.closest('.photo');
      if (!lab) return;
      lab.classList.toggle('has', !!photos[k]);
      var clearBtn = $('[data-clear=' + k + ']', lab);
      if (clearBtn) clearBtn.hidden = !photos[k];
    });
  }

  $$('[data-photo]').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var f = inp.files && inp.files[0];
      if (!f) return;
      var k = inp.getAttribute('data-photo');
      var max = k === 'cover_image' ? 520 : 420;
      var img = new Image();
      var url = URL.createObjectURL(f);
      img.onload = function () {
        var s = Math.min(1, max / Math.max(img.width, img.height));
        var c = document.createElement('canvas');
        c.width = Math.round(img.width * s);
        c.height = Math.round(img.height * s);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        photos[k] = c.toDataURL('image/jpeg', 0.68);
        URL.revokeObjectURL(url);
        syncPhotos();
        schedulePreview();
      };
      img.src = url;
      inp.value = '';
    });
  });

  $$('[data-clear]').forEach(function (b) {
    b.addEventListener('click', function (e) {
      e.preventDefault();
      delete photos[b.getAttribute('data-clear')];
      syncPhotos();
      schedulePreview();
    });
  });

  /* ---------- Wire UI Events ---------- */
  form.addEventListener('input', schedulePreview);
  form.addEventListener('change', schedulePreview);

  // Occasion card clicks
  $$('.occasion-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var occ = card.getAttribute('data-occ');
      if (occ) setOccasion(occ);
    });
  });

  // Palette card clicks
  $$('.palette-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var pal = card.getAttribute('data-pal');
      if (pal) setPalette(pal);
    });
  });

  // Device switcher clicks (Phone / Tablet / Laptop)
  $$('.device-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var dev = btn.getAttribute('data-dev');
      $$('.device-btn').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var prev = $('#preview');
      if (prev) {
        prev.classList.remove('is-phone', 'is-tablet', 'is-laptop');
        prev.classList.add('is-' + dev);
      }
    });
  });

  // Events add button
  var evAddBtn = $('#evAdd');
  if (evAddBtn) {
    evAddBtn.onclick = function () {
      var n = addEventRow({});
      if (n) {
        var inp = $('input', n);
        if (inp) inp.focus();
      }
      schedulePreview();
    };
  }

  // Events preset dropdown
  var evPresetSel = $('#evPreset');
  if (evPresetSel) {
    evPresetSel.onchange = function () {
      if (!this.value) return;
      addEventRow({ name: this.value, date: form.event_date.value });
      this.value = '';
      schedulePreview();
    };
  }

  // Reset & Clear buttons
  if ($('#resetBtn')) {
    $('#resetBtn').onclick = function () {
      setOccasion(currentOccasion);
    };
  }
  if ($('#clearBtn')) {
    $('#clearBtn').onclick = function () {
      loadData({ events: [], music_enabled: true });
      schedulePreview();
    };
  }

  /* ---------- Create & Dispatch Modal Logic ---------- */
  function showErr(t) {
    var e = $('#err');
    if (e) {
      e.textContent = t;
      e.hidden = !t;
    }
  }

  if ($('#createBtn')) {
    $('#createBtn').onclick = function () {
      var d = collectData();
      var miss = [];
      if (!d.groom_name) miss.push("First Host / Celebrant Name");
      if (!d.event_date) miss.push("Event Date");
      if (!d.venue) miss.push("Venue");

      if (miss.length) {
        showErr('Please fill required fields: ' + miss.join(', '));
        var first = form.querySelector(':invalid');
        if (first) {
          first.closest('details').open = true;
          first.focus();
        }
        return;
      }
      showErr('');

      window.JFYCodec.encode(d).then(function (s) {
        var u = new URL('invite.html', location.href);
        u.search = '';
        u.hash = 'data=' + s;
        var fullLink = u.toString();

        $('#shareUrl').value = fullLink;
        $('#openLink').href = fullLink;

        // Trigger guest update
        if (window.updateGuestLink) window.updateGuestLink();

        $('#sheet').hidden = false;
      });
    };
  }

  if ($('#copyBtn')) {
    $('#copyBtn').onclick = function () {
      var i = $('#shareUrl');
      var b = this;
      i.select();
      var ok = function () {
        b.textContent = 'Copied ✓';
        setTimeout(function () { b.textContent = 'Copy Link'; }, 2000);
      };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(i.value).then(ok, ok);
      } else {
        document.execCommand('copy');
        ok();
      }
    };
  }

  if ($('#sheetX')) {
    $('#sheetX').onclick = function () {
      $('#sheet').hidden = true;
    };
  }

  /* ---------- Initial Boot ---------- */
  // Check if hash has data
  var hashMatch = /[#&]data=([^&]+)/.exec(location.hash);
  if (hashMatch && window.JFYCodec) {
    window.JFYCodec.decode(hashMatch[1]).then(function (decoded) {
      if (decoded.occasion_type) currentOccasion = decoded.occasion_type;
      setOccasion(currentOccasion, true);
      loadData(decoded);
      schedulePreview();
    });
  } else {
    // Check localStorage draft or default
    try {
      var saved = localStorage.getItem(DRAFT_KEY);
      if (saved) {
        var parsed = JSON.parse(saved);
        if (parsed.occasion_type) currentOccasion = parsed.occasion_type;
        setOccasion(currentOccasion, true);
        loadData(parsed);
        schedulePreview();
      } else {
        setOccasion('wedding');
      }
    } catch (_) {
      setOccasion('wedding');
    }
  }

})();
