/* JFY share-link codec: JSON <-> URL-safe string. "z." prefix = deflate-raw compressed, otherwise plain base64. */
(function () {
  function b64u(bytes) { var s = ''; for (var i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000)); return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''); }
  function unb64u(str) { str = str.replace(/-/g, '+').replace(/_/g, '/'); while (str.length % 4) str += '='; var bin = atob(str), out = new Uint8Array(bin.length); for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i); return out; }
  async function pipe(bytes, stream) { var s = new Blob([bytes]).stream().pipeThrough(stream); return new Uint8Array(await new Response(s).arrayBuffer()); }
  window.JFYCodec = {
    encode: async function (obj) {
      var bytes = new TextEncoder().encode(JSON.stringify(obj));
      if (window.CompressionStream) { try { return 'z.' + b64u(await pipe(bytes, new CompressionStream('deflate-raw'))); } catch (e) {} }
      return b64u(bytes);
    },
    decode: async function (str) {
      str = decodeURIComponent(str);
      if (str.indexOf('z.') === 0) return JSON.parse(new TextDecoder().decode(await pipe(unb64u(str.slice(2)), new DecompressionStream('deflate-raw'))));
      return JSON.parse(new TextDecoder().decode(unb64u(str)));
    }
  };
})();
