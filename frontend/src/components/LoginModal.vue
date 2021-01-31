<template lang="html">
  <section class="modal" :class="{'is-active': is_login_visible}">
    <div class="modal-background"></div>
    <div class="modal-content is-success">
      <div class="box is-success">

          <h2 class="title is-3">Login</h2>

          <div class="field">
            <label for="email">Courriel: </label>
            <div class="control">
              <input class="input" type="email" name="email" placeholder="armand.guidon@gmail.com">
            </div>
          </div>

          <div class="field">
            <label for="password">Mot de pass: </label>
            <div class="control">
              <input class="input" type="password" name="password">
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button type="button" name="button" class="button is-success">Login</button>
            </div>
          </div>

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
      "SET_IS_LOGIN_VISIBLE"
    ])
  }
}
</script>

<style lang="css" scoped>

</style>
