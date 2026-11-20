/* GoldenVows Celebration Studio — Data Loader & Dynamic Occasion Initializer */
(function () {
  'use strict';

  var PRESETS = window.OCCASION_PRESETS || {};
  var DEFAULT_PRESET = PRESETS.wedding || window.JFY_DATA || {};

  var OCCASION_CONFIG = {
    wedding: {
      typeLabel: "Royal Wedding Invitation",
      callLabel: "Incoming Wedding Call",
      eyebrow: "you are cordially invited<br>to the royal wedding of",
      heartSymbol: "❤",
      hostsTitle: "Meet The Couple",
      hostsSubtitle: "Two hearts, one beautiful journey together.",
      c1Role: "The Groom",
      c2Role: "The Bride",
      eventsTitle: "Wedding Ceremonies & Itinerary",
      saveDateScript: "The Wedding Day",
      footThanks: "Thank you for being part of our wedding celebration",
      calSuffix: " — Wedding",
      rsvpMsg: "Congratulations! We can't wait to celebrate your wedding.",
      defaultPalette: "emerald-gold"
    },
    housewarming: {
      typeLabel: "Griha Pravesh & Housewarming Invitation",
      callLabel: "Incoming Housewarming Invitation",
      eyebrow: "you are cordially invited<br>to the Griha Pravesh &amp; Housewarming of",
      heartSymbol: "🏡",
      hostsTitle: "The Family & Our New Abode",
      hostsSubtitle: "A sanctuary built with love, prayers and elder blessings.",
      c1Role: "Head of Family",
      c2Role: "New Residence",
      eventsTitle: "Auspicious Puja & Ceremonies",
      saveDateScript: "The Auspicious Day",
      footThanks: "Thank you for gracing our new home with your warm blessings",
      calSuffix: " — Griha Pravesh",
      rsvpMsg: "Congratulations on your new home! Excited to celebrate your Griha Pravesh.",
      defaultPalette: "terracotta-marigold"
    },
    babyshower: {
      typeLabel: "Baby Shower & Godh Bharai Invitation",
      callLabel: "Incoming Baby Shower Call",
      eyebrow: "you are warmly invited<br>to the Baby Shower &amp; Godh Bharai of",
      heartSymbol: "🍼",
      hostsTitle: "Meet The Parents-to-be",
      hostsSubtitle: "Welcoming our little miracle with love, laughter and blessings.",
      c1Role: "Father-to-be",
      c2Role: "Mother-to-be",
      eventsTitle: "Baby Shower Schedule & Games",
      saveDateScript: "The Celebration Day",
      footThanks: "Thank you for showering our little one with love and blessings",
      calSuffix: " — Baby Shower",
      rsvpMsg: "Congratulations! So thrilled to celebrate the baby shower with you.",
      defaultPalette: "pastel-cloud"
    },
    birthday: {
      typeLabel: "Birthday Celebration Invitation",
      callLabel: "Incoming Birthday Party Call",
      eyebrow: "you are cordially invited<br>to celebrate the Birthday of",
      heartSymbol: "🎂",
      hostsTitle: "The Birthday Star",
      hostsSubtitle: "Celebrating another milestone year of joy, dreams and laughter.",
      c1Role: "Birthday Star",
      c2Role: "Milestone Celebration",
      eventsTitle: "Party Schedule & Highlights",
      saveDateScript: "The Big Party",
      footThanks: "Thank you for bringing your sparkle to our birthday bash",
      calSuffix: " — Birthday Party",
      rsvpMsg: "Happy Birthday! Looking forward to rocking the party with you.",
      defaultPalette: "wine-rose"
    },
    engagement: {
      typeLabel: "Engagement & Ring Ceremony Invitation",
      callLabel: "Incoming Ring Ceremony Call",
      eyebrow: "you are cordially invited<br>to the Engagement &amp; Ring Ceremony of",
      heartSymbol: "💍",
      hostsTitle: "Meet The Couple",
      hostsSubtitle: "A promise of forever begins with this sacred ring.",
      c1Role: "The Fiancé",
      c2Role: "The Fiancée",
      eventsTitle: "Engagement Ceremonies & Schedule",
      saveDateScript: "The Ring Ceremony",
      footThanks: "Thank you for celebrating our engagement with love",
      calSuffix: " — Engagement",
      rsvpMsg: "Congratulations on your engagement! Can't wait to toast with you.",
      defaultPalette: "midnight-star"
    },
    anniversary: {
      typeLabel: "Anniversary Celebration Invitation",
      callLabel: "Incoming Anniversary Call",
      eyebrow: "you are cordially invited<br>to celebrate the Anniversary of",
      heartSymbol: "🥂",
      hostsTitle: "The Loving Couple",
      hostsSubtitle: "Celebrating decades of unconditional love and togetherness.",
      c1Role: "The Husband",
      c2Role: "The Wife",
      eventsTitle: "Anniversary Celebrations & Schedule",
      saveDateScript: "The Anniversary Day",
      footThanks: "Thank you for honoring our years of love and companionship",
      calSuffix: " — Anniversary",
      rsvpMsg: "Happy Anniversary! Wishing you endless years of joy and happiness.",
      defaultPalette: "emerald-gold"
    }
  };

  function finalize(d) {
    d = d || {};
    var occasionKey = (d.occasion_type || 'wedding').toLowerCase();
    var cfg = OCCASION_CONFIG[occasionKey] || OCCASION_CONFIG.wedding;
    var base = PRESETS[occasionKey] || DEFAULT_PRESET;

    // Merge missing fields from occasion defaults
    Object.keys(base).forEach(function (k) {
      if (d[k] === undefined || d[k] === null || d[k] === '') {
        d[k] = base[k];
      }
    });

    // Populate dynamic occasion-specific tokens
    if (!d.theme_palette) d.theme_palette = cfg.defaultPalette;
    if (!d.occasion_title) d.occasion_title = cfg.typeLabel;
    d.call_label = cfg.callLabel;
    d.heart_icon = cfg.heartSymbol;
    d.hero_eyebrow = d.invite_eyebrow || cfg.eyebrow;
    d.hosts_title = cfg.hostsTitle;
    d.hosts_subtitle = cfg.hostsSubtitle;
    d.celebrant_1_role = cfg.c1Role;
    d.celebrant_2_role = cfg.c2Role;
    d.events_title = cfg.eventsTitle;
    d.save_date_script = cfg.saveDateScript;
    d.foot_thanks = cfg.footThanks;
    d.cal_suffix = cfg.calSuffix;
    d.rsvp_default_msg = cfg.rsvpMsg;

    // Build dynamic page title
    var gName = d.groom_name || 'Celebrant';
    var bName = d.bride_name || '';
    if (occasionKey === 'housewarming') {
      d.page_title = (d.groom_full_name || gName) + ' — ' + d.occasion_title;
    } else if (occasionKey === 'birthday') {
      d.page_title = gName + ' — ' + d.occasion_title;
    } else {
      d.page_title = gName + (bName ? ' & ' + bName : '') + ' — ' + d.occasion_title;
    }

    if (d.music_enabled === false) d.music_url = '';
    if (d.show_gallery === false) d.gallery = [];
    if (!d.venue_map_url && d.venue) {
      d.venue_map_url = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(d.venue + ' ' + (d.venue_address || ''));
    }

    (d.events || []).forEach(function (e) {
      if (e.time && e.date && e.date.indexOf('T') < 0) e.date = e.date + 'T' + e.time;
      if (!e.map_url && (e.venue || d.venue)) {
        e.map_url = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent((e.venue || d.venue) + ' ' + (d.venue_address || ''));
      }
    });

    if (d.event_time && d.event_date && d.event_date.indexOf('T') < 0) {
      d.event_date = d.event_date + 'T' + d.event_time;
    }

    // Apply palette to body early
    if (d.theme_palette && document.body) {
      document.body.setAttribute('data-palette', d.theme_palette);
      document.body.classList.add('palette-' + d.theme_palette);
    }

    return d;
  }

  // Parse hash #data=...
  var m = /[#&]data=([^&]+)/.exec(location.hash);
  window.JFY_READY = (m && window.JFYCodec ? JFYCodec.decode(m[1]).then(function (decoded) {
    window.JFY_DATA = finalize(Object.assign({}, decoded));
  }) : Promise.resolve(window.JFY_DATA ? finalize(window.JFY_DATA) : finalize(DEFAULT_PRESET)))
  .catch(function (e) {
    console.warn('Invitation data could not be read, using default preset.', e);
    window.JFY_DATA = finalize(DEFAULT_PRESET);
  });
})();
