<template>
  <div>
    <h1>Pick Lunch</h1>
    <div>
      <h2>{{ menu }}</h2>
      <button @click="pickMenu">위이이잉..!</button>
    </div>
    <div>
      <h2>로또도 뽑아보자!</h2>
      <button @click="moveToLotto">로..또..?</button>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LunchView',
  data() {
    return {
      menus: ['카레', '치킨', '새우튀김', '등심덧살',],
      menu: ''
    }
  },
  methods: {
    pickMenu() {
      this.menu = _.sample(this.menus)
    },
    moveToLotto() {
      this.$router.push({ name: 'lotto', params: { count: 6 } })
    }
  },
  created() {
    this.pickMenu()
  }
}
</script>

<style>

</style>