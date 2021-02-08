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
    radius: 500,
    is_logged: false,
    is_login_visible: false,
    is_register_visible: false,
    register_error_message: "",
    token_key: null

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
    },
    SET_IS_LOGGED: (state, new_value) => {
      state.is_logged = new_value
    },
    SET_IS_LOGIN_VISIBLE: (state, new_value) => {
      state.is_login_visible = new_value
    },
    SET_IS_REGISTER_VISIBLE: (state, new_value) => {
      state.is_register_visible = new_value
    },
    SET_REGISTER_ERROR_MESSAGE: (state, new_value) => {
      state.register_error_message = new_value
    },
    SET_TOKEN_KEY: (state, new_value) => {
      state.token_key = new_value
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

    },

    register: (context, registerForm) => {
      return axios.post("/auth/register/", registerForm).then( response => {
        console.log(response.data)
        context.commit("SET_REGISTER_ERROR_MESSAGE", "")
      }).catch(error => {
        console.log(error.response.data)
        context.commit("SET_REGISTER_ERROR_MESSAGE", error.response.data)
      })
    },

    login: (context, loginForm) => {
      return axios.post("/auth/login/", loginForm).then( response => {
        context.commit("SET_IS_LOGGED", true)
        context.commit("SET_TOKEN_KEY", response.data.key)
      })
    },

    loginGoogle: (context, code)=> {
      return axios.post("/auth/google/", code).then( response => {
        context.commit("SET_IS_LOGGED", true)
        context.commit("SET_TOKEN_KEY", response.data.key)
      }).catch(error => {
        console.log(error.response.data)
      })
    },

    logout: (context) => {
      return axios.post("/auth/logout/",null,context.getters.headers).then(response => {
        context.commit("SET_IS_LOGGED", false)
        context.commit("SET_TOKEN_KEY", null)
      })
    },

    resetPassword: (context, email) => {
      return axios.post("/auth/password/reset", email).then(() => {

      }).catch(() => {

      })

    }


  },
  getters: {
      headers: state => {
        if(state.is_logged){
          return {
            'Authorization': 'TOKEN ' + state.token_key
          }
        }else {
          return {}
        }
      }
  }
})
