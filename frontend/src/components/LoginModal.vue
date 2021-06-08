<template lang="html">
  <section class="modal" :class="{'is-active': is_login_visible}">
    <div class="modal-background"></div>
    <div class="modal-content is-success">
      <div class="box is-success" id="loginbox">

          <h2 class="title is-3">S'authentifier</h2>

          <div class="field">
            <label for="email">Courriel : </label>
            <div class="control">
              <input class="input" type="email" name="email" placeholder="armand.guidon@gmail.com" v-model="email">
            </div>
          </div>

          <div class="field">
            <label for="password">Mot de passe : </label>
            <div class="control">
              <input class="input" type="password" name="password" v-model="password">
            </div>
          </div>
          <div v-if="login_error_message" class="notification is-danger">
            {{ login_error_message }}
          </div>


          <div class="buttons">
              <button @click="initLogin" type="button" name="button" class="button is-success">S'authentifier</button>
              <button @click="showRegisterModal" type="button" name="button" class="button is-info">S'inscrire</button>
              <button type="button" class="button is-text">Oublie de mot de passe ?</button>
          </div>
          <a class="button is-danger is-fullwidth" :href="google_login_url" >S'authentifier avec Google</a>
          <br>
          <a class="button is-link is-fullwidth" :href="facebook_login_url" >S'authentifier avec Facebook</a>

      </div>

    </div>
    <button @click="SET_IS_LOGIN_VISIBLE(false)" class="modal-close is-large" aria-label="close"></button>
  </section>

</template>

<script>
import { mapState , mapMutations , mapActions } from 'vuex';
export default {
  props: ["google_login_url" , "facebook_login_url"],
  data: function(){
    return {
      email: "",
      password: "",
      login_error_message: ""
    }
  },
  computed: {
    ...mapState([
      "is_login_visible"
    ])
  },
  methods: {
    ...mapMutations([
      "SET_IS_LOGIN_VISIBLE",
      "SET_IS_REGISTER_VISIBLE"
    ]),

    ...mapActions([
      "login",
      "loginGoogle"
    ]),

    initLogin: function(){
      const loginForm = {
        "email": this.email,
        "password": this.password
      }

      this.login(loginForm).then(()=>{
        this.SET_IS_LOGIN_VISIBLE(false)
        this.email = ""
        this.password = ""
        this.login_error_message = "";
      }).catch(error => {
        this.login_error_message = "Le mot de passe et/ou le courriel est incorrect."
      })
    },

    showRegisterModal: function(){
      this.SET_IS_LOGIN_VISIBLE(false)
      this.SET_IS_REGISTER_VISIBLE(true)
    }
  }
}
</script>

<style lang="css" scoped>

</style>
