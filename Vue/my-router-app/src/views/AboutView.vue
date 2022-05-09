<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="moveToHome">home</button>
  </div>
</template>

<script>

export default {
  name: 'AboutView',
  methods: {
    moveToHome() {
      this.$router.push({ name: 'home' })
    }
  }
}
</script>
