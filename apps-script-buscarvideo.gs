// Búsqueda de candidatos de video para la app (opcional). Se pega UNA vez en el Apps Script de la hoja.
// 1) Crea una clave de la "YouTube Data API v3" en Google Cloud (gratis) y guárdala en
//    Configuración del proyecto > Propiedades del script > YT_KEY.
// 2) En doPost, antes de responder una acción desconocida, agrega:
//      if (d.a === 'buscarvideo') return ContentService.createTextOutput(JSON.stringify(buscarVideo_(d))).setMimeType(ContentService.MimeType.JSON);
//    (y verifica el PIN del coach igual que en 'listar' si quieres limitarlo).
// La app solo muestra los candidatos: el coach elige, nunca se pone uno solo.
function buscarVideo_(d) {
  var key = PropertiesService.getScriptProperties().getProperty('YT_KEY');
  if (!key) return { ok: false, error: 'sin-clave' };
  var q = String(d.q || '').slice(0, 120); if (!q) return { ok: false, error: 'vacio' };
  var url = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&videoEmbeddable=true&maxResults=3&relevanceLanguage=es&q=' + encodeURIComponent(q) + '&key=' + key;
  var r = JSON.parse(UrlFetchApp.fetch(url, { muteHttpExceptions: true }).getContentText());
  if (r.error) return { ok: false, error: 'youtube' };
  return { ok: true, items: (r.items || []).map(function(x) {
    return { id: x.id.videoId, title: x.snippet.title, channel: x.snippet.channelTitle, thumb: (x.snippet.thumbnails.medium || x.snippet.thumbnails.default).url };
  }) };
}
