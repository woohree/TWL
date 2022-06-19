<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input type="text" id="username" required v-model="credentials.username"/>
      </div>
      <div>
        <label for="password1">Password: </label>
        <input type="password" id="password1" required v-model="credentials.password1"/>
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input type="password" id="password2" required v-model="credentials.password2"/>
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    components: {
      AccountErrorList,
    },
    name: 'SignupView',
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
