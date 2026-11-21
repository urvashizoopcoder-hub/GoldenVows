/* GoldenVows & Royal Palace Unified Editor Engine
 * Full live synchronization with:
 * 1. Grand Palace Balcony Hero Page (Image 3)
 * 2. Meet The Couple Section (Image 4)
 * 3. Save The Date Envelope & 4 Heart-Shaped Countdown Timers (Image 1)
 * 4. Auspicious Royal Arched Card & Ceremonies Timeline (Image 2)
 * 5. Soft Indian Instrumental Background Music & Smooth Auto-Scrolling Engine
 */
(function () {
  'use strict';

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var SAMPLE = window.JFY_DATA || {
    groom_name: "Ranveer",
    groom_full_name: "Ranveer Mittal",
    groom_parents: "Son of Mr. Sunil Mittal & Mrs. Rekha Mittal",
    bride_name: "Shanaya",
    bride_full_name: "Shanaya Jindal",
    bride_parents: "Daughter of Mr. Navin Jindal & Mrs. Savitri Jindal",
    event_date: "2027-11-25T19:00",
    venue: "The Taj Mahal Palace Ballroom, Mumbai",
    venue_address: "Apollo Bunder, Colaba, Mumbai, Maharashtra 400001",
    venue_map_url: "https://www.google.com/maps/search/?api=1&query=The+Taj+Mahal+Palace+Mumbai",
    couple_quote: "Two souls, one promise — bound by seven sacred vows and a lifetime of laughter.",
    invite_message: "Together with their families, Ranveer & Shanaya request the honour of your presence at their wedding celebrations.",
    hashtag: "#RanveerWedsShanaya",
    events: [
      { name: "The Sangeet Spectacular", date: "2027-11-24T19:00", venue: "The Crystal Ballroom, Taj Mahal Palace", map_url: "https://www.google.com/maps/search/?api=1&query=The+Taj+Mahal+Palace+Mumbai", dress: "Diamond Sparkle & Royal Velvet" },
      { name: "Baraat & Varmala Ceremony", date: "2027-11-25T17:30", venue: "Gateway of India Promenade", map_url: "https://www.google.com/maps/search/?api=1&query=Gateway+of+India+Mumbai", dress: "Royal Indian Aristocratic" },
      { name: "Sacred Pheras & Matrimony", date: "2027-11-25T19:30", venue: "Grand Mandap Hall, Taj Mahal Palace", map_url: "https://www.google.com/maps/search/?api=1&query=The+Taj+Mahal+Palace+Mumbai", dress: "Gold Zardozi & Pure Silk" },
      { name: "Royal Governors Reception", date: "2027-11-26T20:00", venue: "The Ballroom, Taj Mahal Palace", map_url: "https://www.google.com/maps/search/?api=1&query=The+Taj+Mahal+Palace+Mumbai", dress: "Ultra Formal Black Tie" }
    ]
  };

  var TEXT = ['groom_name','groom_full_name','groom_parents','bride_name','bride_full_name','bride_parents','venue','venue_address','venue_map_url','invite_message','couple_quote','closing_quote','family_signoff','hashtag','rsvp_whatsapp','rsvp_deadline'];
  var PHOTOS = ['groom_photo','bride_photo','cover_image'];
  var form = $('#ed');
  var photos = {};
  var pvTimer = null;
  var countdownTimer = null;
  var autoScrollTimer = null;
  var isAutoScrolling = false;
  var userInteracting = false;
  var resumeTimer = null;

  function split(dt) {
    var m = /^(\d{4}-\d{2}-\d{2})(?:T(\d{2}:\d{2}))?/.exec(dt || '');
    return m ? [m[1], m[2] || ''] : ['', ''];
  }

  /* ---------- fill form from data ---------- */
  function load(d) {
    if (!form) return;
    TEXT.forEach(function (k) { if (form[k]) form[k].value = d[k] || ''; });
    var dt = split(d.event_date);
    if (form.event_date) form.event_date.value = dt[0];
    if (form.event_time) form.event_time.value = d.event_time || dt[1];
    if (form.music_enabled) form.music_enabled.checked = d.music_enabled !== false;
    if (form.show_gallery) form.show_gallery.checked = d.show_gallery !== false;

    photos = {};
    PHOTOS.forEach(function (k) {
      if (d[k] && /^data:/.test(d[k])) photos[k] = d[k];
    });
    syncPhotos();

    var evList = $('#evList');
    if (evList) {
      evList.innerHTML = '';
      (d.events || []).forEach(addEvent);
      renumber();
    }

    syncLiveTemplateDOM(d);
  }

  function addEvent(e) {
    e = e || {};
    var tpl = $('#evTpl');
    if (!tpl) return;
    var node = tpl.content.firstElementChild.cloneNode(true);
    var dt = split(e.date);
    var nName = $('[data-k=name]', node); if (nName) nName.value = e.name || '';
    var nDate = $('[data-k=date]', node); if (nDate) nDate.value = dt[0];
    var nTime = $('[data-k=time]', node); if (nTime) nTime.value = e.time || dt[1];
    var nVen = $('[data-k=venue]', node); if (nVen) nVen.value = e.venue || '';
    var nMap = $('[data-k=map_url]', node); if (nMap) nMap.value = e.map_url || '';
    var nDress = $('[data-k=dress]', node); if (nDress) nDress.value = e.dress || '';

    var del = $('.ev__del', node);
    if (del) {
      del.onclick = function () {
        node.remove();
        renumber();
        schedule();
      };
    }
    var evList = $('#evList');
    if (evList) {
      evList.appendChild(node);
      renumber();
    }
    return node;
  }

  function renumber() {
    $$('#evList .ev').forEach(function (n, i) {
      var no = $('.ev__no', n);
      if (no) no.textContent = 'Event ' + (i + 1);
    });
  }

  /* ---------- read form into data ---------- */
  function collect() {
    if (!form) return SAMPLE;
    var d = {};
    TEXT.forEach(function (k) {
      if (form[k]) {
        var v = (form[k].value || '').trim();
        if (v) d[k] = v;
      }
    });
    if (d.rsvp_whatsapp) d.rsvp_whatsapp = d.rsvp_whatsapp.replace(/\D/g, '');
    if (form.event_date && form.event_date.value) {
      d.event_date = form.event_date.value + (form.event_time && form.event_time.value ? 'T' + form.event_time.value : '');
    }
    if (form.music_enabled && !form.music_enabled.checked) d.music_enabled = false;
    if (form.show_gallery && !form.show_gallery.checked) d.show_gallery = false;

    PHOTOS.forEach(function (k) {
      if (photos[k]) d[k] = photos[k];
    });

    d.events = $$('#evList .ev').map(function (n) {
      var g = function (k) { return ($('[data-k=' + k + ']', n) ? $('[data-k=' + k + ']', n).value : '').trim(); };
      var e = { name: g('name') };
      if (!e.name) return null;
      if (g('date')) e.date = g('date') + (g('time') ? 'T' + g('time') : '');
      ['venue', 'map_url', 'dress'].forEach(function (k) { if (g(k)) e[k] = g(k); });
      return e;
    }).filter(Boolean);

    return d;
  }

  /* ================= 4 Heart Countdown Engine ================= */
  function initHeartCountdown(dateStr) {
    if (countdownTimer) clearInterval(countdownTimer);

    function update() {
      var target = new Date(dateStr);
      var now = new Date();
      var diff = target.getTime() - now.getTime();

      var days = 85, hours = 9, minutes = 58, seconds = 45;
      if (!isNaN(diff) && diff > 0) {
        days = Math.floor(diff / (1000 * 60 * 60 * 24));
        hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        seconds = Math.floor((diff % (1000 * 60)) / 1000);
      }

      var elDays = $('#cdDays'); if (elDays) elDays.textContent = String(days);
      var elHours = $('#cdHours'); if (elHours) elHours.textContent = String(hours).padStart(2, '0');
      var elMins = $('#cdMinutes'); if (elMins) elMins.textContent = String(minutes).padStart(2, '0');
      var elSecs = $('#cdSeconds'); if (elSecs) elSecs.textContent = String(seconds).padStart(2, '0');
    }

    update();
    countdownTimer = setInterval(update, 1000);
  }

  /* ================= Interactive Envelope Toggle ================= */
  window.toggleSaveDateEnvelope = function () {
    var wrap = $('#stdEnvelopeWrapper');
    if (!wrap) return;
    var isOpen = wrap.classList.toggle('open');
    var prompt = $('#envelopePrompt');
    if (prompt) {
      prompt.textContent = isOpen ? '✨ Tap again to close the royal envelope' : 'Tap the envelope to open it.';
    }
    if (isOpen) {
      if (typeof window.triggerMagicSparkles === 'function') {
        window.triggerMagicSparkles();
      }
      var audio = $('#bgMusic');
      if (audio && audio.paused) {
        audio.volume = 0.35;
        audio.play().catch(function () {});
      }
    }
  };

  /* ================= Soft Indian Instrumental Audio Engine ================= */
  window.toggleMusic = function () {
    var audio = $('#bgMusic');
    var btn = $('#btnMusicToggle') || $('.btn-music-toggle');
    if (!audio) return;
    if (audio.paused) {
      audio.volume = 0.35; // Soft gentle sitar
      audio.play().then(function () {
        if (btn) btn.innerHTML = '🎵 Music: ON';
      }).catch(function () {});
    } else {
      audio.pause();
      if (btn) btn.innerHTML = '🔇 Music: OFF';
    }
  };

  /* ================= Smooth Continuous Auto-Scrolling Engine ================= */
  window.startAutoScroll = function () {
    if (autoScrollTimer) clearInterval(autoScrollTimer);
    isAutoScrolling = true;
    var btn = $('#btnAutoScroll') || $('.btn-autoscroll-toggle');
    if (btn) btn.innerHTML = '⏸ Pause Scroll';

    autoScrollTimer = setInterval(function () {
      if (!userInteracting && isAutoScrolling) {
        window.scrollBy({ top: 1.2, behavior: 'smooth' });
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight - 40) {
          window.stopAutoScroll();
        }
      }
    }, 32);
  };

  window.stopAutoScroll = function () {
    isAutoScrolling = false;
    if (autoScrollTimer) clearInterval(autoScrollTimer);
    var btn = $('#btnAutoScroll') || $('.btn-autoscroll-toggle');
    if (btn) btn.innerHTML = '▶ Auto Scroll';
  };

  window.toggleAutoScroll = function () {
    if (isAutoScrolling) {
      window.stopAutoScroll();
    } else {
      window.startAutoScroll();
    }
  };

  // Pause on user touch, resume 2.5s after user stops
  window.addEventListener('touchstart', function () {
    userInteracting = true;
    clearTimeout(resumeTimer);
  }, { passive: true });

  window.addEventListener('touchend', function () {
    clearTimeout(resumeTimer);
    resumeTimer = setTimeout(function () { userInteracting = false; }, 2500);
  }, { passive: true });

  window.addEventListener('wheel', function () {
    userInteracting = true;
    clearTimeout(resumeTimer);
    resumeTimer = setTimeout(function () { userInteracting = false; }, 2500);
  }, { passive: true });

  /* ================= Modal Dispatch Sheet ================= */
  window.closeSheet = function () {
    var s = $('#sheet');
    if (s) s.hidden = true;
  };

  /* ================= Live Preview DOM Synchronizer ================= */
  function syncLiveTemplateDOM(d) {
    d = d || collect();
    var gName = d.groom_name || 'Ranveer';
    var bName = d.bride_name || 'Shanaya';
    var gFull = d.groom_full_name || gName + ' Mittal';
    var bFull = d.bride_full_name || bName + ' Jindal';
    var gPar = d.groom_parents || 'Son of Mr. Sunil Mittal & Mrs. Rekha Mittal';
    var bPar = d.bride_parents || 'Daughter of Mr. Navin Jindal & Mrs. Savitri Jindal';
    var ven = d.venue || 'The Taj Mahal Palace Ballroom, Mumbai';
    var evDt = d.event_date || '2027-11-25T19:00';

    var dateObj = new Date(evDt.includes('T') ? evDt : evDt + 'T12:00:00');
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    var dayStr = isNaN(dateObj.getTime()) ? 'THURSDAY' : days[dateObj.getDay()].toUpperCase();
    var dateNum = isNaN(dateObj.getTime()) ? '25TH' : dateObj.getDate() + 'TH';
    var monthStr = isNaN(dateObj.getTime()) ? 'NOV' : months[dateObj.getMonth()].toUpperCase();
    var yearStr = isNaN(dateObj.getTime()) ? '2027' : dateObj.getFullYear();
    var dateBadge = dayStr + ' | ' + dateNum + ' ' + monthStr + ' ' + yearStr;
    var dateFormal = dayStr + ', ' + dateNum + ' ' + monthStr + ' ' + yearStr;

    // 1. Hero Palace Balcony Page (Image 3)
    var hG = $('#heroGroomName'); if (hG) hG.textContent = gFull;
    var hB = $('#heroBrideName'); if (hB) hB.textContent = bFull;
    var hD = $('#heroDateBadge'); if (hD) hD.textContent = dateBadge;

    // 2. Meet The Couple Page (Image 4)
    var dG = $('#displayGroomName'); if (dG) dG.textContent = gFull;
    var dB = $('#displayBrideName'); if (dB) dB.textContent = bFull;
    var dGP = $('#displayGroomParents'); if (dGP) dGP.textContent = gPar;
    var dBP = $('#displayBrideParents'); if (dBP) dBP.textContent = bPar;
    var dQuote = $('#displayCoupleQuote');
    if (dQuote) dQuote.textContent = d.couple_quote || '“Two souls, one promise — bound by seven sacred vows and a lifetime of laughter.”';

    // 3. Save The Date Envelope & Letter (Image 1)
    var letCouple = $('#letterCoupleNames'); if (letCouple) letCouple.textContent = gName + ' & ' + bName;
    var letDate = $('#letterEventDate'); if (letDate) letDate.textContent = dateFormal;
    var letVen = $('#letterVenue'); if (letVen) letVen.textContent = ven;
    var waxInitials = $('#waxSealInitials');
    if (waxInitials) {
      waxInitials.textContent = (gName ? gName[0] : 'R') + ' & ' + (bName ? bName[0] : 'S');
    }

    // 4. Live 4 Heart-Shaped Countdown
    initHeartCountdown(evDt);

    // 5. Auspicious Royal Arched Card (Image 2)
    var archG = $('#archedGroomName'); if (archG) archG.textContent = gName;
    var archB = $('#archedBrideName'); if (archB) archB.textContent = bName;
    var archDT = $('#archedDateTime');
    if (archDT) {
      var timePart = d.event_time || (evDt.includes('T') ? evDt.split('T')[1] : '19:00');
      var ymd = evDt.split('T')[0];
      archDT.textContent = ymd + ' · ' + timePart;
    }
    var archV = $('#archedVenue'); if (archV) archV.textContent = ven.toUpperCase();
    var archBless = $('#archedBlessingText');
    if (archBless) {
      archBless.textContent = 'Together with their families, ' + gName + ' & ' + bName + ' request the honour of your presence at the solemn matrimonial union.';
    }

    // Scratch Card
    var scratchD = $('#scratchDateTitle'); if (scratchD) scratchD.textContent = dateFormal;
    var scratchV = $('#scratchVenueSubtitle') || $('.unveiled-time-venue');
    if (scratchV) scratchV.textContent = (d.event_time ? d.event_time + ' · ' : '7:00 PM · ') + ven;
    var sGName = $('#scratchGroomName'); if (sGName) sGName.textContent = gName;
    var sBName = $('#scratchBrideName'); if (sBName) sBName.textContent = bName;

    // Photos
    if (photos.groom_photo && $('#displayGroomPhoto')) $('#displayGroomPhoto').src = photos.groom_photo;
    if (photos.bride_photo && $('#displayBridePhoto')) $('#displayBridePhoto').src = photos.bride_photo;
    if (photos.groom_photo && $('#scratchGroomImg')) $('#scratchGroomImg').src = photos.groom_photo;
    if (photos.bride_photo && $('#scratchBrideImg')) $('#scratchBrideImg').src = photos.bride_photo;

    // 6. Timeline Sacred Functions with Corner Flowers & Sequential Entrance
    var timelineGrid = $('.timeline-grid') || $('#timelineGrid');
    if (timelineGrid && d.events && d.events.length > 0) {
      var cornerTL = '<svg class="floral-corner top-left" viewBox="0 0 60 60" fill="none"><defs><radialGradient id="roseG_card" cx="35%" cy="35%" r="65%"><stop offset="0%" stop-color="#fda4af"/><stop offset="45%" stop-color="#f43f5e"/><stop offset="85%" stop-color="#be123c"/><stop offset="100%" stop-color="#881337"/></radialGradient><linearGradient id="goldG_card" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#fef08a"/><stop offset="50%" stop-color="#d4af37"/><stop offset="100%" stop-color="#854d0e"/></linearGradient></defs><path d="M 0 16 C 12 18, 22 26, 28 40" stroke="url(#goldG_card)" stroke-width="1.3" stroke-linecap="round"/><path d="M 16 0 C 18 12, 26 22, 40 28" stroke="url(#goldG_card)" stroke-width="1.3" stroke-linecap="round"/><path d="M 16 12 C 20 7, 26 6, 28 10 C 25 16, 19 17, 16 12 Z" fill="#047857" stroke="#d4af37" stroke-width="0.7"/><path d="M 12 16 C 7 20, 6 26, 10 28 C 16 25, 17 19, 12 16 Z" fill="#047857" stroke="#d4af37" stroke-width="0.7"/><circle cx="14" cy="14" r="12" fill="url(#roseG_card)" filter="drop-shadow(0 2px 5px rgba(0,0,0,0.45))"/><path d="M 7 14 C 7 9, 12 5, 15 5 C 19 5, 22 9, 21 14 C 19 17, 12 17, 7 14 Z" fill="#fda4af" opacity="0.85"/><path d="M 10 11 C 12 7, 17 7, 19 11 C 21 14, 15 17, 12 15 Z" fill="#f43f5e"/><path d="M 12 12 C 13 10, 16 10, 17 12 C 17 15, 14 16, 12 12 Z" fill="#9f1239"/><circle cx="14" cy="12.5" r="2" fill="#fef08a"/><circle cx="28" cy="10" r="5.5" fill="url(#roseG_card)"/><path d="M 26 8 C 27 6, 31 7, 31 9 C 30 11, 27 10, 26 8 Z" fill="#fda4af"/><circle cx="10" cy="28" r="5.5" fill="url(#roseG_card)"/><path d="M 8 26 C 6 27, 7 31, 9 31 C 11 30, 10 27, 8 26 Z" fill="#fda4af"/><circle cx="36" cy="13" r="1.3" fill="#fef08a"/><circle cx="13" cy="36" r="1.3" fill="#fef08a"/></svg>';
      var cornerTR = cornerTL.replace('class="floral-corner top-left"', 'class="floral-corner top-right"');
      var cornerBL = cornerTL.replace('class="floral-corner top-left"', 'class="floral-corner bottom-left"');
      var cornerBR = cornerTL.replace('class="floral-corner top-left"', 'class="floral-corner bottom-right"');

      var html = '';
      d.events.forEach(function (ev, i) {
        var eDt = split(ev.date);
        html += '<div class="timeline-card function-reveal-item" data-index="' + i + '">' +
          cornerTL + cornerTR + cornerBL + cornerBR +
          '<div class="timeline-card-inner">' +
            '<div class="timeline-step-badge">FUNCTION ' + (i + 1) + '</div>' +
            '<h3 class="ceremony-name-heading">' + (ev.name || 'Ceremony') + '</h3>' +
            '<p class="ceremony-time-text">📅 ' + (eDt[0] || '2027-11-25') + (eDt[1] ? ' · ' + eDt[1] : '') + '</p>' +
            '<p class="ceremony-venue-text">📍 ' + (ev.venue || ven) + '</p>' +
            (ev.dress ? '<p class="ceremony-dress-text">👗 <b>Attire:</b> ' + ev.dress + '</p>' : '') +
            (ev.map_url ? '<a href="' + ev.map_url + '" target="_blank" rel="noopener" class="ceremony-map-btn">🗺️ Open Map</a>' : '') +
          '</div>' +
        '</div>';
      });
      timelineGrid.innerHTML = html;
      if (typeof window.revealFunctionsOneByOne === 'function') {
        window.revealFunctionsOneByOne();
      }
    }
  }

  function schedule() {
    clearTimeout(pvTimer);
    pvTimer = setTimeout(function () {
      var d = collect();
      syncLiveTemplateDOM(d);
    }, 150);
  }

  if (form) {
    form.addEventListener('input', schedule);
    form.addEventListener('change', schedule);
  }

  /* ---------- photo inputs ---------- */
  function syncPhotos() {
    $$('[data-photo]').forEach(function (inp) {
      var k = inp.getAttribute('data-photo');
      var lab = inp.closest('.photo');
      if (!lab) return;
      lab.classList.toggle('has', !!photos[k]);
      var btn = $('.photo__btn', lab);
      if (btn) btn.textContent = photos[k] ? '✓ Photo added' : 'Upload';
      var x = $('[data-clear=' + k + ']', lab);
      if (x) x.hidden = !photos[k];
    });
  }

  $$('[data-photo]').forEach(function (inp) {
    inp.addEventListener('change', function () {
      var f = inp.files && inp.files[0];
      if (!f) return;
      var k = inp.getAttribute('data-photo');
      var max = 500;
      var img = new Image();
      var url = URL.createObjectURL(f);
      img.onload = function () {
        var s = Math.min(1, max / Math.max(img.width, img.height));
        var c = document.createElement('canvas');
        c.width = Math.round(img.width * s);
        c.height = Math.round(img.height * s);
        c.getContext('2d').drawImage(img, 0, 0, c.width, c.height);
        photos[k] = c.toDataURL('image/jpeg', 0.75);
        URL.revokeObjectURL(url);
        syncPhotos();
        schedule();
      };
      img.src = url;
    });
  });

  $$('[data-clear]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var k = btn.getAttribute('data-clear');
      delete photos[k];
      var inp = $('[data-photo=' + k + ']');
      if (inp) inp.value = '';
      syncPhotos();
      schedule();
    });
  });

  /* ---------- presets & events ---------- */
  var evAdd = $('#evAdd');
  if (evAdd) evAdd.addEventListener('click', function () { addEvent(); schedule(); });

  var evPreset = $('#evPreset');
  if (evPreset) {
    evPreset.addEventListener('change', function () {
      var val = evPreset.value;
      if (!val) return;
      var baseDate = (form && form.event_date && form.event_date.value) || '2027-11-25';
      var presets = {
        'Haldi': { time: '10:00', dress: 'Yellow & Marigold Traditional' },
        'Mehendi': { time: '15:00', dress: 'Floral Lehengas & Kurtas' },
        'Sangeet': { time: '19:00', dress: 'Royal Velvet & Sparkling Diamonds' },
        'Wedding': { time: '17:30', dress: 'Traditional Aristocratic Silk' },
        'Reception': { time: '20:00', dress: 'Ultra Formal Black Tie' },
        'Engagement': { time: '18:00', dress: 'Elegance & Champagne Gold' },
        'Cocktail': { time: '20:30', dress: 'Glamorous Evening Chic' }
      };
      var p = presets[val] || {};
      addEvent({ name: val, date: baseDate + (p.time ? 'T' + p.time : ''), dress: p.dress || '' });
      evPreset.value = '';
      schedule();
    });
  }

  /* ---------- action buttons ---------- */
  var resetBtn = $('#resetBtn');
  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      load(SAMPLE);
    });
  }

  var clearBtn = $('#clearBtn');
  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (form) form.reset();
      photos = {};
      syncPhotos();
      var evList = $('#evList');
      if (evList) evList.innerHTML = '';
      syncLiveTemplateDOM({});
    });
  }

  /* ---------- initial load ---------- */
  document.addEventListener('DOMContentLoaded', function () {
    load(SAMPLE);
  });
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    load(SAMPLE);
  }

})();
