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
      lmarkers: [],
      center: null,
      map: null,
      tileLayer: null,
      parkingsLayer: null
    }
  },

  computed: {
      ...mapState([
        "coords",
        "bike_parkings",
        "radius"
      ]),

      circle: function(){
        return L.circle(this.coords, this.radius)
      }
  },

  mounted: function() {

    this.center = L.circle(this.coords, {radius: this.radius})
    this.map = L.map('map', {
      center: this.coords,
      zoom: 15}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.center.addTo(this.map);

    this.parkingsLayer = L.layerGroup(this.lmarkers).addTo(this.map)

    this.map.on("click", this.map_click);
    this.getLocation();
  },

  created: function() {
    //this.getLocation()
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

    }
  },
  watch: {
    bike_parkings: function(){


      this.lmarkers.splice(0, this.lmarkers.length);

      this.parkingsLayer.clearLayers();
      this.bike_parkings.forEach((marker, index) => {
        const lmarker = L.marker([marker.position.coordinates[1], marker.position.coordinates[0]]);
        //this.lmarkers.push(lmarker);
        this.parkingsLayer.addLayer(lmarker)
      });


    },

    coords: function(){
      console.log("coord");
      this.map.panTo(this.coords)
      this.center.setLatLng(this.coords)
      this.getBikeParkings()

    },

  }

}

</script>
<style lang="scss" scoped>
  //$margin: 0.4rem;

  #map {
    margin: 0;
    z-index: 0;
    height: 100%;
    width: 100%;
    position: fixed;
  }
</style>
