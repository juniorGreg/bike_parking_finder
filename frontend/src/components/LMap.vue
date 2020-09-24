<template>
  <div id="map">

  </div>

</template>

<script>
import L from 'leaflet';


export default {
  name: "l-map",
  data: function(){
    return {
      lmarkers: []
    }
  },
  props: ['markers', "coords", "radius"],
  mounted: function() {
    console.log(this.markers);
    L.Icon.Default.imagePath = '/static/';
    this.map = L.map('map', {
      center: [45.5016889, -73.567256],
      zoom: 13}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.center = L.circle(this.coords, {radius: this.radius}).addTo(this.map);

    this.map.on("click", this.map_click);
  },
  methods: {
    map_click: function(e){
      this.$emit("mapClick", [e.latlng.lat, e.latlng.lng]);
      console.log(e.latlng.lat);
    }
  },
  watch: {
    markers: function(){
      console.log("update");
      let map = this.map;
      let lmarkers = this.lmarkers;

      this.lmarkers.forEach(function(lmarker, index){
        map.removeLayer(lmarker);
      });

      this.lmarkers.splice(0, this.lmarkers.length);

      function updateMarkers(marker, index){
        let lmarker = L.marker([marker.position.coordinates[1], marker.position.coordinates[0]]).addTo(map);
        lmarkers.push(lmarker);
      }

      this.markers.forEach(updateMarkers);
    },
    coords: function(){
      this.center.setLatLng(this.coords);
      this.map.setView(this.coords);
    },
    radius: function(){
      console.log(this.radius);
      this.center.setRadius(this.radius);
    }
  }

}

</script>
<style lang="scss" scoped>
  $margin: 0.4rem;

  #map {
    margin: $margin;
    height: calc(100% - 2*#{$margin});
    width: calc(100% - 2*#{$margin});
  }
</style>
