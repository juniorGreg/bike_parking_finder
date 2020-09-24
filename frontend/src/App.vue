<template>
  <div id="app">
    <section class="hero is-warning">
      <div class="hero-body">
        <div class="container">
            <h1 class="title">Bike Parking Finder</h1>
        </div>
      </div>

    </section>
    <LMap :radius="this.radius" :markers="this.bike_parkings" :coords="this.coords" @mapClick="updateCoords">

  </div>
</template>

<script>

import LMap from "./components/LMap.vue"
import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'



export default {
  name: 'App',
  components : {
    LMap
  },
  data: function() {
    return {
        bike_parkings: [],
        coords: [45.501688, -73.567256],
        radius: 500
      }
  },
  watch: {
    coords: function(){
      this.getBikeParkings(this.coords[0], this.coords[1]);
    }
  },
  methods: {
    getBikeParkings: function(lat, lng){
      axios.get('/api/bike_parkings?radius='+this.radius+'&lat='+lat+'&lng='+lng).then(response=>{
        this.bike_parkings = response.data
      })
    },
    getLocation: function(){
      if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(this.showPosition);
      }
    },
    showPosition: function(position){
      let lat= position.coords.latitude;
      let lng= position.coords.longitude;
      this.coords = [lat, lng];
      //this.getBikeParkings(lat, lng);
    },
    updateCoords: function(e) {
      this.coords = e;
    }
  },
  mounted: function() {
    this.getLocation();
    //this.getBikeParkings();
  }

}
</script>

<style lang="scss">
@import "~bulma/bulma";
  html{
    height: 100vh;
  }
  body {
    background-color: $warning;
    min-height: 100vh;
    width: 100%;
  }
  #app {
    height: calc(100vh - 8.5rem);
  }
</style>
