<template>
  <div>
    <nav class="navbar is-fixed-top" role="navigation" aria-label="navigation principale">
        <div class="navbar-brand">
          <div class="navbar-item">
            <img :src="logo" alt="Logo de parkmonbaïk">
          </div>
          <a role="button" @click="toggleNavBar" class="navbar-burger" :class="{'is-active': is_navbar_visible}" aria-label="menu" aria-expanded="false" data-target="navbarParkMonBaik">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>

        </div>
        <div id="navbarParkMonBaik" class="navbar-menu" :class="{'is-active': is_navbar_visible}">
          <div class="navbar-start">
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">Mode temps réel</a>
              <div class="navbar-dropdown">
                <div class="navbar-item">
                  <div class="field">
                    <input id="modeRealTime" type="checkbox" name="modeRealTime" class="switch">
                    <label for="modeRealTime">Off</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <button @click="loginAction" class="button is-success">{{login_button_text}}</button>
            </div>
          </div>
        </div>
    </nav>
    <LoginModal></LoginModal>
    <main>

        <LMap></LMap>
    </main>



  </div>
</template>

<script>

import LMap from "./components/LMap.vue"
import LoginModal from "./components/LoginModal.vue"


import { mapState , mapMutations , mapActions } from 'vuex';


export default {
  name: 'App',
  props: ["logo"],
  components : {
    LMap,
    LoginModal
  },
  data: function(){
    return {
      is_navbar_visible: false
    }
  },
  computed: {
    ...mapState([
      "is_logged"
    ]),
    login_button_text: function(){
      if(this.is_logged){
          return "Logout"
      }else {
          return "Login"
      }


    }
  },
  methods: {
    ...mapMutations([
      "SET_IS_LOGIN_VISIBLE"
    ]),
    loginAction: function(){
      if(this.is_logged){
        console.log("logout")
      }else{
        this.SET_IS_LOGIN_VISIBLE(true)
      }
    },
    toggleNavBar: function(){
      this.is_navbar_visible = !this.is_navbar_visible
    }
  }

}
</script>

<style lang="scss">

</style>
