import './mystyles.scss';



import Vue from 'vue'
import App from './App.vue'
import 'leaflet/dist/leaflet.css';

import store from './store'


new Vue({
  store: store,
  render: h => h(App),
}).$mount('#app')
