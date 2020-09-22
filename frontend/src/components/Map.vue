<template>
  <div id="map">

  </div>

</template>

<script>
import L from 'leaflet';

export default {
  data: function(){
    return {
      //map: L.map('map').setView([0,0], 1)
    }
  },
  mounted() {
    L.Icon.Default.imagePath = '/static/';
    this.map = L.map('map', {
      center: [45.5016889, -73.567256],
      zoom: 13}
    );
    this.tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);
    this.center = L.marker([45.5016889, -73.567256]).addTo(this.map);
  }
}

</script>
<style scoped>
  #map {
    padding: 3em;
    min-height: 100%;
    width: 100%;
  }
</style>
