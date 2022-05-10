<template>
  <div id="app" class="border-box-blue">
    <h1>App</h1>
    <input type="text" v-model="appInput">
    <p>From Parent => {{ parentInput }}</p>
    <p>From Child => {{ childInput }}</p>
    <the-parent :app-input="appInput" @change-parent-input="getParentInput" @change-child-input="getChildInput"></the-parent>
  </div>
</template>

<script>
import TheParent from '@/components/TheParent.vue'

export default {
  name: 'App',
  components: {
    TheParent,
  },
  data() {
    return {
      appInput: '',
      parentInput: '',
      childInput: '',
    }
  },
  methods: {
    getParentInput(parentInput) {
      this.parentInput = parentInput
    },
    getChildInput(childInput) {
      this.childInput = childInput
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

.border-box-blue {
  border: 2px solid rgb(49, 49, 231);
  margin: 3px;
}
</style>
