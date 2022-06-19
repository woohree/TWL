<template>
  <div>
    <h1>Login</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <div>
        <label for="username">username: </label>
        <input type="text" id="username" required v-model="credentials.username"/>
      </div>

      <div>
        <label for="password">password: </label>
        <input type="password" id="password" required v-model="credentials.password"/>
      </div>

      <button>Login</button>
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
    name: 'LoginView',
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style></style>
