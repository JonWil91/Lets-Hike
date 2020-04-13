// Initialising LeafletJS Map

var mapTileLayers = L.tileLayer("http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}", {
    attribution: "Powered by <a href='https://developers.arcgis.com/terms/attribution/' target='_blank' rel='noopener'>Esri</a>"
});

var map = L.map("map", {
    layers: [mapTileLayers],
    center: [53.8008, 1.5491],
    zoom: 5
});

// Customised icons

let scotIcon = new L.Icon({
    iconUrl: "static/images/scotflag.png",
    iconSize: [25, 25],
    iconAnchor: [12, 25]
});

let engIcon = new L.Icon({
    iconUrl: "static/images/engflag.png",
    iconSize: [25, 25],
    iconAnchor: [12, 25]
});

let walesIcon = new L.Icon({
    iconUrl: "static/images/walesflag.png",
    iconSize: [25, 25],
    iconAnchor: [12, 25]
});

// Markers for the three highest peaks in UK

const myScotMarker = L.marker([56.796956, -5.003272], {icon: scotIcon}).addTo(map).bindTooltip("Ben Nevis");

const myEnglandMarker = L.marker([54.595270, -3.195633], {icon: engIcon}).addTo(map).bindTooltip("Scarfell Pike");

const myWalesMarker = L.marker([53.073936, -4.076236], {icon: walesIcon}).addTo(map).bindTooltip("Snowden");








