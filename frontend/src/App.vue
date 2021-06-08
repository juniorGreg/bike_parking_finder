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
                    <input id="modeRealTime" type="checkbox" name="modeRealTime" class="switch" disabled>
                    <label for="modeRealTime">Off</label>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <button @click="loginAction" class="button" :class="login_class">{{login_button_text}}</button>
            </div>
          </div>
        </div>
    </nav>
    <LoginModal :google_login_url="google_login_url" :facebook_login_url="facebook_login_url"></LoginModal>
    <RegisterModal :google_recaptcha_site="google_recaptcha_site"></RegisterModal>
    <main>

        <LMap></LMap>
    </main>



  </div>
</template>

<script>

import LMap from "./components/LMap.vue"
import LoginModal from "./components/LoginModal.vue"
import RegisterModal from "./components/RegisterModal.vue"


import { mapState , mapMutations , mapActions } from 'vuex';


export default {
  name: 'App',
  props: ["logo", "google_recaptcha_site", "google_login_url", "google_code", "facebook_login_url", "facebook_code"],
  components : {
    LMap,
    LoginModal,
    RegisterModal
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
    },

    login_class: function(){
      if(this.is_logged){
          return "is-danger"
      }else {
          return "is-success"
      }
    }
  },
  methods: {
    ...mapMutations([
      "SET_IS_LOGIN_VISIBLE"
    ]),
    ...mapActions([
      "logout",
      "loginGoogle",
      "loginFacebook",
      "checkLoginState"
    ]),
    loginAction: function(){
      if(this.is_logged){
        this.logout()
      }else{
        this.SET_IS_LOGIN_VISIBLE(true)
      }
    },
    toggleNavBar: function(){
      this.is_navbar_visible = !this.is_navbar_visible
    }
  },

  created: function(){
    this.checkLoginState()

    if(this.google_code){
      const code = {
        'code': this.google_code
      }

      this.loginGoogle(code)
    }

    if(this.facebook_code){
      const code = {
        'code': this.facebook_code
      }

      this.loginFacebook(code)
    }
  }

}
</script>

<style lang="scss">

</style>
