<template lang="html">
  <section class="modal" :class="{'is-active': is_login_visible}">
    <div class="modal-background"></div>
    <div class="modal-content is-success">
      <div class="box is-success">

          <h2 class="title is-3">S'authentifier</h2>

          <div class="field">
            <label for="email">Courriel : </label>
            <div class="control">
              <input class="input" type="email" name="email" placeholder="armand.guidon@gmail.com">
            </div>
          </div>

          <div class="field">
            <label for="password">Mot de passe : </label>
            <div class="control">
              <input class="input" type="password" name="password">
            </div>
          </div>

          <div class="buttons">
              <button @click="showRegisterModal" type="button" name="button" class="button is-info">S'incrire</button>
              <button type="button" name="button" class="button is-success">S'authentifier</button>

          </div>
          <button class="button is-danger is-fullwidth" type="button" name="button">Google</button>
          <br>
          <button class="button is-link is-fullwidth" type="button" name="button">Facebook</button>

      </div>

    </div>
    <button @click="SET_IS_LOGIN_VISIBLE(false)" class="modal-close is-large" aria-label="close"></button>
  </section>

</template>

<script>
import { mapState , mapMutations , mapActions } from 'vuex';
export default {
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

    showRegisterModal: function(){
      this.SET_IS_LOGIN_VISIBLE(false)
      this.SET_IS_REGISTER_VISIBLE(true)
    }
  }
}
</script>

<style lang="css" scoped>

</style>
