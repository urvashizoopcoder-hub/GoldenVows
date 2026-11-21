/**
 * GoldenVows — Universal Template Customization Synchronizer
 * Automatically reflects studio form customizations (Bride/Groom names,
 * color palette, date, venue, opening experience, particles) across all 60 templates.
 */
(function () {
  'use strict';

  var PALETTES = {
    'emerald-gold': {
      '--wine': '#064E3B', '--wine-d': '#022C22', '--rose': '#047857', '--rose-d': '#065F46',
      '--gold': '#D4AF37', '--gold-l': '#FDE68A', '--blush': '#F6F3EB', '--blush2': '#EFEAD8',
      '--ivory': '#FCFBF7', '--ink': '#132A13', '--ink-l': '#374151'
    },
    'wine-rose': {
      '--wine': '#831843', '--wine-d': '#500724', '--rose': '#BE185D', '--rose-d': '#9D174D',
      '--gold': '#EAB308', '--gold-l': '#FEF08A', '--blush': '#FDF2F8', '--blush2': '#FCE7F3',
      '--ivory': '#FFF1F2', '--ink': '#4C0519', '--ink-l': '#701A35'
    },
    'midnight-star': {
      '--wine': '#1E1B4B', '--wine-d': '#0F0E2A', '--rose': '#4338CA', '--rose-d': '#3730A3',
      '--gold': '#D97706', '--gold-l': '#FDE68A', '--blush': '#EEF2FF', '--blush2': '#E0E7FF',
      '--ivory': '#F8FAFC', '--ink': '#1E1B4B', '--ink-l': '#312E81'
    },
    'pastel-cloud': {
      '--wine': '#0284C7', '--wine-d': '#0369A1', '--rose': '#EC4899', '--rose-d': '#DB2777',
      '--gold': '#FACC15', '--gold-l': '#FEF08A', '--blush': '#FDF2F8', '--blush2': '#F0F9FF',
      '--ivory': '#FFFFFF', '--ink': '#0C4A6E', '--ink-l': '#1E3A8A'
    },
    'terracotta-marigold': {
      '--wine': '#9A3412', '--wine-d': '#6C2209', '--rose': '#C2410C', '--rose-d': '#9A3412',
      '--gold': '#EAB308', '--gold-l': '#FEF08A', '--blush': '#FFFBEB', '--blush2': '#FEF3C7',
      '--ivory': '#FFFDF5', '--ink': '#451A03', '--ink-l': '#78350F'
    }
  };

  function syncTemplate() {
    var d = null;

    // 1. Check localStorage for active studio customizations
    try {
      var saved = localStorage.getItem('gv_active_invite');
      if (saved) d = JSON.parse(saved);
    } catch (_) {}

    // Fallback to draft key if gv_active_invite is empty
    if (!d) {
      try {
        var draft = localStorage.getItem('goldenvows_draft_v2');
        if (draft) d = JSON.parse(draft);
      } catch (_) {}
    }

    if (!d) d = {};

    // 2. Query parameter overrides
    var q = new URLSearchParams(window.location.search);
    if (q.get('groom')) d.groom_name = q.get('groom');
    if (q.get('bride')) d.bride_name = q.get('bride');
    if (q.get('date')) d.event_date = q.get('date');
    if (q.get('venue')) d.venue = q.get('venue');
    if (q.get('palette')) d.theme_palette = q.get('palette');
    if (q.get('opener')) d.opening_style = q.get('opener');
    if (q.get('particles')) d.ambient_particles = q.get('particles');

    var gName = d.groom_name || '';
    var bName = d.bride_name || '';
    var couple = gName ? (bName ? (gName + ' & ' + bName) : gName) : '';

    // 3. Reflect Color Palette
    var palKey = d.theme_palette;
    if (palKey && PALETTES[palKey]) {
      var pal = PALETTES[palKey];
      var root = document.documentElement;
      Object.keys(pal).forEach(function (prop) {
        root.style.setProperty(prop, pal[prop]);
      });
      if (document.body && !document.body.classList.contains('cartier-dark-mode')) {
        document.body.style.backgroundColor = pal['--blush2'];
        document.body.style.color = pal['--ink'];
      }
    }

    // 4. Reflect Couple Names
    if (couple) {
      document.title = couple + ' — Wedding Invitation';

      var elCover = document.getElementById('coverCoupleNames');
      if (elCover) elCover.textContent = couple;

      var elStageNames = document.querySelector('.stage-names');
      if (elStageNames) elStageNames.textContent = couple;

      var elBride = document.getElementById('brideNameDisplay');
      if (elBride && bName) elBride.textContent = bName;

      var elGroom = document.getElementById('groomNameDisplay');
      if (elGroom && gName) elGroom.textContent = gName;

      var elLetterSig = document.getElementById('letterSignature');
      if (elLetterSig) elLetterSig.textContent = couple;

      // Update generic template titles
      document.querySelectorAll('.wed-main-title').forEach(function (el) {
        el.textContent = couple;
      });
      document.querySelectorAll('.wed-couple-title').forEach(function (el) {
        el.textContent = couple;
      });
    }

    // 5. Reflect Date
    if (d.event_date) {
      var dateText = d.event_date.replace('T', ' · ');
      var elDate = document.getElementById('weddingDateDisplay');
      if (elDate) elDate.textContent = dateText;

      var elSealDate = document.getElementById('sealDateBig');
      if (elSealDate) elSealDate.textContent = dateText;

      document.querySelectorAll('.wed-date-ribbon').forEach(function (el) {
        el.textContent = dateText;
      });
    }

    // 6. Reflect Venue
    if (d.venue) {
      var elVenue = document.getElementById('weddingVenueDisplay');
      if (elVenue) elVenue.textContent = d.venue.toUpperCase();

      var elVenueAddr = document.getElementById('venueAddressDisplay');
      if (elVenueAddr) elVenueAddr.textContent = d.venue + (d.venue_address ? (', ' + d.venue_address) : '');

      document.querySelectorAll('.wed-venue-tag').forEach(function (el) {
        el.textContent = d.venue;
      });
    }

    // 7. Reflect Opening Style (for templates supporting multiple openers)
    if (d.opening_style) {
      var callEl = document.getElementById('call');
      var envEl = document.getElementById('coverEnv');
      if (d.opening_style === 'envelope') {
        if (envEl) envEl.style.display = 'flex';
        if (callEl) callEl.style.display = 'none';
      } else if (d.opening_style === 'call') {
        if (callEl) callEl.style.display = 'flex';
        if (envEl) envEl.style.display = 'none';
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', syncTemplate);
  } else {
    syncTemplate();
  }

  window.addEventListener('storage', function (e) {
    if (e.key === 'gv_active_invite' || e.key === 'goldenvows_draft_v2') {
      syncTemplate();
    }
  });

  window.syncTemplateCustomizations = syncTemplate;
})();
