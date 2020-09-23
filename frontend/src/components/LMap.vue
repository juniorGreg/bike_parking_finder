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
  props: ['markers', "lat", "long"],
  mounted: function() {
    console.log(this.markers);
    L.Icon.Default.imagePath = '/static/';
    this.map = L.map('map', {
      center: [45.5016889, -73.567256],
      zoom: 13}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.center = L.marker([this.lat, this.long]).addTo(this.map);
  },
  watch: {
    markers: function(){
      console.log("update");
      let map = this.map;
      function updateBikeParking(marker, index){
        L.marker([marker.position.coordinates[1], marker.position.coordinates[0]]).addTo(map);
      }

      this.markers.forEach(updateBikeParking);
    },
    lat: function(){
      this.center.setLatLng([this.lat, this.long]);
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
