import Vue from 'vue';
import Vuex from 'vuex';

import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

Vue.use(Vuex);

export default new Vuex.Store({
  state: () => ({
    bike_parkings: [],
    coords: [45.501688, -73.567256],
    radius: 500
  }),

  mutations: {
    SET_BIKE_PARKINGS: (state, new_value) => {
      state.bike_parkings = new_value
    },

    SET_COORDS: (state, new_value) => {
      state.coords = new_value
    },
    SET_RADIUS: (state, new_value) => {
      state.radius = new_value
    }
  },
  actions: {
    getLocation: (context) => {

      if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition((position) => {
          const lat= position.coords.latitude;
          const lng= position.coords.longitude;
          const coords = [lat, lng];
          context.commit("SET_COORDS", coords)
        });
      }

    },

    getBikeParkings: (context) => {
      const lat = context.state.coords[0]
      const lng = context.state.coords[1]
      return axios.get('/api/bike_parkings?radius='+context.state.radius+'&lat='+lat+'&lng='+lng).then(response=>{
          context.commit("SET_BIKE_PARKINGS", response.data)
      })
    }

  },

  getters: {

  }
})
