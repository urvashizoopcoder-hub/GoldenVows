/* GoldenVows Celebration Studio — Data Loader & Dynamic Occasion Initializer */
(function () {
  'use strict';

  var PRESETS = window.OCCASION_PRESETS || {};
  var DEFAULT_PRESET = PRESETS.wedding || window.JFY_DATA || {};

  var OCCASION_CONFIG = {
    wedding: {
      typeLabel: "Royal Wedding Invitation",
      callLabel: "Incoming Royal Wedding Call",
      eyebrow: "you are cordially invited<br>to the royal wedding of",
      heartSymbol: "❤",
      hostsTitle: "Meet The Couple",
      hostsSubtitle: "Two hearts, one beautiful journey together.",
      c1Role: "The Groom",
      c2Role: "The Bride",
      eventsTitle: "Wedding Ceremonies & Itinerary",
      saveDateScript: "The Wedding Day",
      footThanks: "Thank you for being part of our royal celebration",
      calSuffix: " — Wedding",
      rsvpMsg: "Congratulations! We can't wait to celebrate your wedding.",
      defaultPalette: "emerald-gold"
    },
    housewarming: {
      typeLabel: "Griha Pravesh & Housewarming Invitation",
      callLabel: "Incoming Griha Pravesh Call",
      eyebrow: "॥ ॐ नमो भगवते वास्तुपुरुषाय नमः ॥<br>You are warmly invited to the Griha Pravesh of",
      heartSymbol: "🏡",
      hostsTitle: "The Family & Our New Abode",
      hostsSubtitle: "A sanctuary built with love, prayers and elder blessings.",
      c1Role: "Head of Family",
      c2Role: "New Residence",
      eventsTitle: "Auspicious Puja & Griha Pravesh Schedule",
      saveDateScript: "The Auspicious Day",
      footThanks: "Thank you for gracing our new home with your warm blessings",
      calSuffix: " — Griha Pravesh",
      rsvpMsg: "Congratulations on your new home! Excited to celebrate your Griha Pravesh.",
      defaultPalette: "terracotta-marigold"
    },
    babyshower: {
      typeLabel: "Baby Shower & Godh Bharai Invitation",
      callLabel: "Incoming Baby Shower Call",
      eyebrow: "A sweet little miracle is on the way!<br>You are invited to the Baby Shower of",
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
      typeLabel: "VIP Birthday Celebration Bash",
      callLabel: "Incoming Birthday VIP Call",
      eyebrow: "★ THE ULTIMATE CELEBRATION BASH ★<br>You are cordially invited to celebrate the Birthday of",
      heartSymbol: "🎂",
      hostsTitle: "The Birthday Star",
      hostsSubtitle: "Celebrating another milestone year of greatness, music & cheers.",
      c1Role: "The Birthday Legend",
      c2Role: "",
      eventsTitle: "VIP Party Schedule & Highlights",
      saveDateScript: "Party Night",
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
      eyebrow: "Celebrating Years of Togetherness<br>You are cordially invited to celebrate the Anniversary of",
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

    // ENFORCE STRICT OCCASION PURITY (Never show bride/groom in birthday or housewarming)
    if (occasionKey === 'birthday') {
      if (!d.hero_image || d.hero_image.indexOf('hero_palace') > -1) d.hero_image = 'assets/img/bday_hero.svg';
      if (!d.cover_image || d.cover_image.indexOf('couple_call') > -1) d.cover_image = 'assets/img/bday_cover.svg';
      if (!d.groom_photo || d.groom_photo.indexOf('groom.webp') > -1) d.groom_photo = 'assets/img/bday_star.svg';
      d.bride_photo = '';
      d.bride_name = '';
      d.bride_full_name = '';
      d.bride_parents = '';
      d.ambient_particles = 'confetti';
      if (!d.gallery || !d.gallery.length || d.gallery.some(function(g) { return g.indexOf('gal') > -1; })) {
        d.gallery = ['assets/img/bday_hero.svg', 'assets/img/bday_cover.svg', 'assets/img/bday_star.svg'];
      }
      (d.events || []).forEach(function (ev, idx) {
        if (!ev.image || ev.image.indexOf('ev_') > -1 || ev.image.indexOf('palace') > -1) {
          ev.image = idx === 0 ? 'assets/img/bday_cover.svg' : (idx === 1 ? 'assets/img/bday_hero.svg' : 'assets/img/bday_star.svg');
        }
      });
    } else if (occasionKey === 'housewarming') {
      if (!d.hero_image || d.hero_image.indexOf('hero_palace') > -1) d.hero_image = 'assets/img/house_hero.svg';
      if (!d.cover_image || d.cover_image.indexOf('couple_call') > -1) d.cover_image = 'assets/img/house_cover.svg';
      if (!d.groom_photo || d.groom_photo.indexOf('groom.webp') > -1) d.groom_photo = 'assets/img/house_family.svg';
      if (!d.bride_photo || d.bride_photo.indexOf('bride.webp') > -1) d.bride_photo = 'assets/img/house_residence.svg';
      d.ambient_particles = 'diyas';
      if (!d.gallery || !d.gallery.length || d.gallery.some(function(g) { return g.indexOf('gal') > -1; })) {
        d.gallery = ['assets/img/house_hero.svg', 'assets/img/house_cover.svg', 'assets/img/house_residence.svg', 'assets/img/house_family.svg'];
      }
      (d.events || []).forEach(function (ev, idx) {
        if (!ev.image || ev.image.indexOf('ev_') > -1 || ev.image.indexOf('palace') > -1) {
          ev.image = idx === 0 ? 'assets/img/house_cover.svg' : (idx === 1 ? 'assets/img/house_hero.svg' : 'assets/img/house_residence.svg');
        }
      });
    } else if (occasionKey === 'babyshower') {
      if (!d.hero_image || d.hero_image.indexOf('hero_palace') > -1) d.hero_image = 'assets/img/baby_hero.svg';
      if (!d.cover_image || d.cover_image.indexOf('couple_call') > -1) d.cover_image = 'assets/img/baby_cover.svg';
      if (!d.groom_photo || d.groom_photo.indexOf('groom.webp') > -1) d.groom_photo = 'assets/img/baby_hero.svg';
      if (!d.bride_photo || d.bride_photo.indexOf('bride.webp') > -1) d.bride_photo = 'assets/img/baby_cover.svg';
      d.ambient_particles = 'stars';
      if (!d.gallery || !d.gallery.length || d.gallery.some(function(g) { return g.indexOf('gal') > -1; })) {
        d.gallery = ['assets/img/baby_hero.svg', 'assets/img/baby_cover.svg'];
      }
      (d.events || []).forEach(function (ev, idx) {
        if (!ev.image || ev.image.indexOf('ev_') > -1 || ev.image.indexOf('palace') > -1) {
          ev.image = idx === 0 ? 'assets/img/baby_hero.svg' : 'assets/img/baby_cover.svg';
        }
      });
    }

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
      d.page_title = (d.groom_full_name || gName) + ' — ' + d.occasion_title;
    } else {
      d.page_title = gName + (bName ? ' & ' + bName : '') + ' — ' + d.occasion_title;
    }

    return d;
  }

  // Hook into URL hash or default preset
  var hash = location.hash || '';
  var dataMatch = hash.match(/#data=([^&]+)/);
  if (dataMatch && window.JFYCodec) {
    window.JFY_READY = window.JFYCodec.decode(dataMatch[1]).then(function (decoded) {
      window.JFY_DATA = finalize(Object.assign({}, decoded));
    }).catch(function () {
      window.JFY_DATA = finalize(DEFAULT_PRESET);
    });
  } else {
    window.JFY_READY = Promise.resolve(window.JFY_DATA ? finalize(window.JFY_DATA) : finalize(DEFAULT_PRESET));
  }

})();
