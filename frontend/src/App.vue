<template>
  <div id="app">
    <section class="hero is-warning">
      <div class="hero-body">
        <div class="container">
            <h1 class="title">Bike Parking Finder</h1>
        </div>
      </div>

    </section>
    <LMap></LMap>

  </div>
</template>

<script>

import LMap from "./components/LMap.vue"
import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

import { mapState , mapMutations , mapActions } from 'vuex';


export default {
  name: 'App',
  components : {
    LMap
  },

  computed: {
      ...mapActions({

      })
  },

  watch: {

  },
  methods: {

  },
  mounted: function() {

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
