<template>
  <div>
    <h1>User Profile</h1>
    <p>당신의 ID는 {{ user.userId }}</p>
    <p>당신의 이름은 {{ user.userName }}</p>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  data: function () {
    return {
      user: this.$route.params,
    }
  }
}
</script>

<style>

</style>