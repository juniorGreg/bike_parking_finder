<template lang="html">
  <div class="">
    <nav class="navbar is-fixed-top" role="navigation" aria-label="navigation principale">
        <div class="navbar-brand">
          <div class="navbar-item">
            <img :src="logo" alt="Logo de parkmonbaïk">
          </div>
        </div>
    </nav>
    <main class="section is-large">
        <div class="contents">
          <h1 class="title is-1">Confirmation de couriel</h1>
          <p class="subtitle" :class="{'is-loading': is_loading}">{{text}}</p>
        </div>
    </main>


  </div>
</template>

<script>

import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = 'csrftoken'

export default {
  props: ["logo", "email_key"],
  data: function(){
    return {
      text_confirm: "",
      is_loading: true,
      is_confirmed: false
    }
  },
  computed: {
    text: function() {
      if(this.is_confirmed){
        return "Votre adresse courriel est confirmée. Vous pouvez maintenant fermer cette fenêtre."
      }else{
        return "Désolé, la confirmation de votre adresse courriel a échouée."
      }
    }
  },
  mounted: function() {
    const load = {
      key: this.email_key
    }
    axios.post("/auth/register/verify-email/", load).then(() => {
      this.is_confirmed = true
    }).catch(() => {
      this.is_confirmed = false
    }).finally(() => {
      this.is_loading = false
    })
  }
}
</script>

<style lang="scss" scoped>
main {
  background-color: darkgray;
  .contents {
    max-width: 35rem;
    margin: auto;
  }

}
</style>
