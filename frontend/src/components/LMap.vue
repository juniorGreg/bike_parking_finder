<template>

  <div id="map">

  </div>

</template>

<script>
import L from 'leaflet';
import { mapState , mapMutations , mapActions } from 'vuex';

import "../leaflet-heat.js"

import MarkerPopup from "./MarkerPopup.vue"

import Vue from "vue";

var MarkerPopupComponent = Vue.extend(MarkerPopup)


export default {
  name: "l-map",
  data: function(){
    return {
      lmarkers: [],
      center: null,
      map: null,
      tileLayer: null,
      parkingsLayer: null,
      heatmapLayer: null,
      heatmapEventSource: null,
      heatmap_data: []
    }
  },

  components: {
    MarkerPopup
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

  methods: {
    ...mapActions([
      "getLocation",
      "getBikeParkings"
    ]),

    ...mapMutations([
        "SET_COORDS",

    ]),

    map_click: function(e){
      this.SET_COORDS([e.latlng.lat, e.latlng.lng]);
    },

    update_heatmap: function(e){
      const new_heatmap_data = JSON.parse(e.data);

      console.log(new_heatmap_data);

      new_heatmap_data.forEach((item,index)=>{
          item.push(1)
          this.heatmapLayer.addLatLng(item)
      })



      //heatmapLayer.setData(new_heatmap_data)

    }
  },

  mounted: function() {

    this.center = L.circle(this.coords, {radius: this.radius})
    this.map = L.map('map', {
      center: this.coords,
      zoom: 15}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.map)
    this.center.addTo(this.map);



    this.parkingsLayer = L.layerGroup(this.lmarkers).addTo(this.map)
    this.heatmapLayer = L.heatLayer([],
    {
      radius: 25,
      max: 30,

    }).addTo(this.map)


    this.map.on("click", this.map_click);

    this.getLocation();

    //connect heatmap data
    this.heatmapEventSource = new EventSource("/heatmap");



    this.heatmapEventSource.onmessage = this.update_heatmap
  },

  created: function() {

    //this.getLocation()
  },

  watch: {
    bike_parkings: function(){


      this.lmarkers.splice(0, this.lmarkers.length);

      this.parkingsLayer.clearLayers();
      this.bike_parkings.forEach((marker, index) => {
        const lmarker = L.marker([marker.position.coordinates[1], marker.position.coordinates[0]]);

        var markerPopupInstance = new MarkerPopupComponent({
          propsData: {"marker": marker}
        })

        markerPopupInstance.$mount()
        //this.$refs.container.appendChild(markerPopupInstance.$el)



        lmarker.bindPopup(markerPopupInstance.popup)
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
    height: calc(100vh - 3.1rem);
    width: 100%;
    position: fixed;
  }
</style>
