// Initialising LeafletJS Map

var mapTileLayers = L.tileLayer("http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}", {
    attribution: "Powered by <a href='https://developers.arcgis.com/terms/attribution/' target='_blank' rel='noopener'>Esri</a>"
});

var map = L.map("map", {
    layers: [mapTileLayers],
    center: [54.330606, -2.746197],
    zoom: 5
});














