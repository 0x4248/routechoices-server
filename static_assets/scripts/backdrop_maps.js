var backdropMaps = {
  osm: L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    className: "wms256",
  }),
  "gmap-street": L.tileLayer("https://mt0.google.com/vt/x={x}&y={y}&z={z}", {
    attribution: "&copy; Google",
    className: "wms256",
  }),
  "gmap-hybrid": L.tileLayer(
    "https://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}",
    {
      attribution: "&copy; Google",
      className: "wms256",
    }
  ),
  "gmap-terrain": L.tileLayer(
    "https://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}",
    {
      attribution: "&copy; Google",
      className: "wms256",
    }
  ),
  "topo-fi": L.tileLayer(
    "https://tiles.kartat.kapsi.fi/peruskartta/{z}/{x}/{y}.jpg",
    {
      attribution: "&copy; National Land Survey of Finland",
      className: "wms256",
    }
  ),
  "mapant-fi": L.tileLayer(
    "https://wmts.mapant.fi/wmts_EPSG3857.php?z={z}&x={x}&y={y}",
    {
      attribution: "&copy; MapAnt.fi and National Land Survey of Finland",
      className: "wms256",
    }
  ),
  "topo-no": L.tileLayer(
    "https://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=topo4&zoom={z}&x={x}&y={y}",
    {
      attribution: "",
      className: "wms256",
    }
  ),
  "mapant-no": L.tileLayer("https://mapant.no/osm-tiles/{z}/{x}/{y}.png", {
    attribution: "&copy; MapAnt.no",
    className: "wms256",
  }),
  "mapant-es": L.tileLayer.wms("https://mapant.es/wms", {
    layers: "mapant.es",
    format: "image/png",
    version: "1.3.0",
    transparent: true,
    attribution: "&copy; MapAnt.es",
    className: "wms256",
  }),
  "topo-world": L.tileLayer("https://tile.opentopomap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenTopoMap (CC-BY-SA)",
    className: "wms256",
  }),
  "topo-world-alt": L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}",
    {
      attribution: "&copy; ArcGIS Online",
      className: "wms256",
    }
  ),
};

function cloneLayer(layer) {
  function cloneOptions(options) {
    var ret = {};
    for (var i in options) {
      var item = options[i];
      if (item && item.clone) {
        ret[i] = item.clone();
      } else if (item instanceof L.Layer) {
        ret[i] = cloneLayer(item);
      } else {
        ret[i] = item;
      }
    }
    return ret;
  }

  function cloneInnerLayers(layer) {
    var layers = [];
    layer.eachLayer(function (inner) {
      layers.push(cloneLayer(inner));
    });
    return layers;
  }
  var options = cloneOptions(layer.options);
  // Renderers
  if (layer instanceof L.SVG) {
    return L.svg(options);
  }
  if (layer instanceof L.Canvas) {
    return L.canvas(options);
  }
  // GoogleMutant GridLayer
  if (L.GridLayer.GoogleMutant && layer instanceof L.GridLayer.GoogleMutant) {
    var googleLayer = L.gridLayer.googleMutant(options);
    layer._GAPIPromise.then(function () {
      var subLayers = Object.keys(layer._subLayers);

      for (var i in subLayers) {
        googleLayer.addGoogleLayer(subLayers[i]);
      }
    });
    return googleLayer;
  }
  // Tile layers
  if (layer instanceof L.TileLayer.WMS) {
    return L.tileLayer.wms(layer._url, options);
  }
  if (layer instanceof L.TileLayer) {
    return L.tileLayer(layer._url, options);
  }
  if (layer instanceof L.ImageOverlay) {
    return L.imageOverlay(layer._url, layer._bounds, options);
  }
  // Marker layers
  if (layer instanceof L.Marker) {
    return L.marker(layer.getLatLng(), options);
  }
  if (layer instanceof L.Circle) {
    return L.circle(layer.getLatLng(), layer.getRadius(), options);
  }
  if (layer instanceof L.CircleMarker) {
    return L.circleMarker(layer.getLatLng(), options);
  }
  if (layer instanceof L.Rectangle) {
    return L.rectangle(layer.getBounds(), options);
  }
  if (layer instanceof L.Polygon) {
    return L.polygon(layer.getLatLngs(), options);
  }
  if (layer instanceof L.Polyline) {
    return L.polyline(layer.getLatLngs(), options);
  }
  if (layer instanceof L.GeoJSON) {
    return L.geoJson(layer.toGeoJSON(), options);
  }
  if (layer instanceof L.FeatureGroup) {
    return L.featureGroup(cloneInnerLayers(layer));
  }
  if (layer instanceof L.LayerGroup) {
    return L.layerGroup(cloneInnerLayers(layer));
  }
  throw "Unknown layer, cannot clone this layer. Leaflet-version: " + L.version;
}

function getBaseLayers() {
  return {
    "Open Street Map": cloneLayer(backdropMaps["osm"]),
    "Google Map Street": cloneLayer(backdropMaps["gmap-street"]),
    "Google Map Satellite": cloneLayer(backdropMaps["gmap-hybrid"]),
    "Google Map Terrain": cloneLayer(backdropMaps["gmap-terrain"]),
    "Mapant Finland": cloneLayer(backdropMaps["mapant-fi"]),
    "Mapant Norway": cloneLayer(backdropMaps["mapant-no"]),
    "Mapant Spain": cloneLayer(backdropMaps["mapant-es"]),
    "Topo Finland": cloneLayer(backdropMaps["topo-fi"]),
    "Topo Norway": cloneLayer(backdropMaps["topo-no"]),
    "Topo World (OpenTopo)": cloneLayer(backdropMaps["topo-world"]),
    "Topo World (ArcGIS)": cloneLayer(backdropMaps["topo-world-alt"]),
  };
}
