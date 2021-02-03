<template lang="html">


  <section class="modal" :class="{'is-active': is_register_visible}">
    <div ref="recaptchaScript"></div>
    <div class="modal-background"></div>
    <div class="modal-content">
      <div class="box">
        <h2 class="title is-2">S'inscrire par courriel</h2>

        <form ref="registerForm">


            <div class="field">
              <label class="label" for="email">Courriel</label>
              <div class="control">
                  <input class="input" v-model="email" type="email" name="email" value="arnand.guidon@gmail.com" required>
              </div>
            </div>

            <div class="field">
              <label class="label" for="password1">Entrez votre mot de passe :</label>
              <div class="control">
                  <input  class="input" v-model="password1" type="password" name="password1" required
                  pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Votre mot de passe doit contenir au moins un chiffre, une majuscule et une minuscule et il doit avoir au moins 8 caractères">
              </div>
            </div>

            <div class="field">
              <label class="label" for="email">Entrez à nouveau votre mot de passe :</label>
              <div class="control">
                  <input ref="password2Input" class="input" v-model="password2" type="password" name="password2" required>
              </div>
            </div>

            <button class="button g-recaptcha is-info" type="submit" name="submit" @click="validateForm"
                    :data-sitekey="google_recaptcha_site"
                    data-callback='initRegistration'
                    data-action='submit'>S'inscrire</button>
        </form>
      </div>
    </div>
    <button @click="hideRegisterModal" class="modal-close is-large" aria-label="close"></button>
  </section>

</template>

<script>

import { mapState , mapMutations , mapActions } from 'vuex';

export default {
  props: ["google_recaptcha_site"],
  computed: {
    ...mapState([
      "is_register_visible"
    ]),
  },

  data: function(){
    return {
      email: "",
      password1: "",
      password2: ""
    }
  },

  methods: {
    ...mapMutations([
      "SET_IS_REGISTER_VISIBLE"
    ]),

    ...mapActions([
      "register"
    ]),

    validateForm: function(){
      if(this.password1 != this.password2){
        this.$refs.password2Input.setCustomValidity("Les mots de passe ne correspondent pas.")
      }

      else {
        this.$refs.password2Input.setCustomValidity("")
      }


    },

    initRegistration: function(token){

      if(this.$refs.registerForm.reportValidity()){
        console.log(token)
        const registerForm = {
          email: this.email,
          password1: this.password1,
          password2: this.password2,
          token: token
        }

        this.register(registerForm)

        this.email=""
        this.password1=""
        this.password2=""
      }




    },
    hideRegisterModal: function(){
      this.SET_IS_REGISTER_VISIBLE(false)
    }
  },

  mounted: function() {
    window.register = this.register;

  },


}
</script>

<style lang="css" scoped>
</style>
