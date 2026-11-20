/* GoldenVows Celebration Studio — Data Loader & Occasion Initializer */
(function () {
  'use strict';

  var PRESETS = window.OCCASION_PRESETS || {};
  var DEFAULT_PRESET = PRESETS.wedding || window.JFY_DATA || {};

  function finalize(d) {
    d = d || {};
    var occasion = d.occasion_type || 'wedding';
    var base = PRESETS[occasion] || DEFAULT_PRESET;

    // Merge missing fields from occasion defaults
    Object.keys(base).forEach(function (k) {
      if (d[k] === undefined || d[k] === null || d[k] === '') {
        d[k] = base[k];
      }
    });

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
