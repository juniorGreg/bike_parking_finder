<template>
  <div id="map">

  </div>

</template>

<script>
import L from 'leaflet';
import { mapState , mapMutations , mapActions } from 'vuex';

export default {
  name: "l-map",
  data: function(){
    return {
      lmarkers: []
    }
  },

  computed: {
      ...mapState([
        "coords",
        "bike_parkings",
        "radius"
      ])
  },

  mounted: function() {
    console.log(this.markers);

    this.map = L.map('map', {
      center: this.coords,
      zoom: 13}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.center = L.circle(this.coords, {radius: this.radius}).addTo(this.map);

    this.map.on("click", this.map_click);
  },
  methods: {
    ...mapActions([
      "getLocation",
      "getBikeParkings"
    ]),

    ...mapMutations([
        "SET_COORDS"
    ]),

    map_click: function(e){
      this.SET_COORDS([e.latlng.lat, e.latlng.lng]);
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
