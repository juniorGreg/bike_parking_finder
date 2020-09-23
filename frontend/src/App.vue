<template>
  <div id="app">
    <section class="hero is-warning">
      <div class="hero-body">
        <div class="container">
            <h1 class="title">Bike Parking Finder</h1>
        </div>
      </div>

    </section>
    <LMap :markers="this.bike_parkings" :lat="this.lat" :long="this.long">

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
        lat: 45.501688,
        long: -73.567256
      }
  },
  methods: {
    getBikeParkings: function(){
      axios.get('/api/bike_parkings/2').then(response=>{
        this.bike_parkings = response.data
      })
    },
    getLocation: function(){
      if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(this.showPosition);
      }
    },
    showPosition: function(position){
      this.lat= position.coords.latitude;
      this.long=position.coords.longitude;
    }
  },
  mounted: function() {
    this.getLocation();
    this.getBikeParkings();
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
