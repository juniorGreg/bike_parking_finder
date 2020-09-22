<template>
  <div id="app">
    <section class="hero is-warning">
      <div class="hero-body">
        <div class="container">
            <h1 class="title">Bike Parking Finder</h1>
        </div>
      </div>

    </section>
    <Map>

  </div>
</template>

<script>

import Map from "./components/Map.vue"


export default {
  name: 'App',
  components : {
    Map
  }

}
</script>

<style lang="scss">
  html{
    height: 100vh;
  }
  body {
    min-height: 100vh;
    width: 100%;
  }
  #app {
    height: calc(100vh - 8.5rem);
  }
</style>
