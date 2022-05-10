<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기, print -->
    <!-- 카멜 케이스 -->
    <!-- <TheAbout :my-message='parentData'/> -->
    <!-- 케밥 케이스 -->
    <the-about :my-message='parentData' @child-input-change='ParentGetChange'></the-about>
  </div>
</template>

<script>
// 1. 불러오기, import
import TheAbout from './components/TheAbout.vue' // import에 변수명 지정 from에 경로

export default {
  name: 'App',
  // 2. 등록하기, resister
  components: {
    TheAbout,
  },
  data() {
    return {
      parentData: 'This!! is!! parent!!'
    }
  },
  methods: {
    ParentGetChange(inputData) {
      console.log('boss', '들린다!! 들린다고!!', inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
