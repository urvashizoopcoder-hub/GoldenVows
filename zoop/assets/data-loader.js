/* Loads invitation data: #data=<encoded JSON> (from the editor's share link) overrides the demo sample.
   Artwork/music defaults are kept so a shared link only needs the text fields. */
(function () {
  var SAMPLE = window.JFY_DATA || {};
  var ASSETS = { hero_image: SAMPLE.hero_image, cover_image: SAMPLE.cover_image, groom_photo: SAMPLE.groom_photo, bride_photo: SAMPLE.bride_photo, gallery: SAMPLE.gallery, music_url: SAMPLE.music_url, music_credit: SAMPLE.music_credit };
  var PRESET = { haldi: 'ev_haldi', mehendi: 'ev_mehendi', mehndi: 'ev_mehendi', sangeet: 'ev_sangeet', wedding: 'ev_wedding', shaadi: 'ev_wedding', phera: 'ev_wedding', reception: 'ev_reception', engagement: 'ev_reception', cocktail: 'ev_sangeet' };
  function finalize(d) {
    Object.keys(ASSETS).forEach(function (k) { if (d[k] == null || d[k] === '') d[k] = ASSETS[k]; });
    if (d.music_enabled === false) d.music_url = '';
    if (d.show_gallery === false) d.gallery = [];
    if (!d.venue_map_url && d.venue) d.venue_map_url = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(d.venue + ' ' + (d.venue_address || ''));
    (d.events || []).forEach(function (e) {
      if (!e.image) { var n = String(e.name || '').toLowerCase(), hit = Object.keys(PRESET).filter(function (k) { return n.indexOf(k) > -1; })[0]; e.image = 'assets/img/' + (hit ? PRESET[hit] : 'ev_wedding') + '.webp'; }
      if (e.time && e.date && e.date.indexOf('T') < 0) e.date = e.date + 'T' + e.time;
    });
    if (d.event_time && d.event_date && d.event_date.indexOf('T') < 0) d.event_date = d.event_date + 'T' + d.event_time;
    return d;
  }
  var m = /[#&]data=([^&]+)/.exec(location.hash);
  window.JFY_READY = (m && window.JFYCodec ? JFYCodec.decode(m[1]).then(function (d) { window.JFY_DATA = finalize(Object.assign({}, d)); }) : Promise.resolve())
    .catch(function (e) { console.warn('Invitation data could not be read, showing the demo.', e); });
})();
