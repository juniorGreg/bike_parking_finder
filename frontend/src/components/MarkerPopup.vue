<template lang="html">
  <div class="container">
    <p class="title is-5">{{marker.name}}</p>
    <p>{{marker.description}}</p>
    <p>Nombre de places : {{marker.capacity}}</p>
    <button class="button is-small is-danger" name="button" @click="indicateInvalidPlace">Place invalide</button>
  </div>

</template>

<script>
import L from 'leaflet';
export default {
  data: function(){
    return {
      popup: null,
    }
  },

  props: ["marker"],

  methods: {
    indicateInvalidPlace: function(){
      console.log("invalid")
    }
  },

  mounted: function(){
    this.popup = L.popup().setContent(this.$el)
  }
}
</script>

<style lang="css" scoped>
</style>
