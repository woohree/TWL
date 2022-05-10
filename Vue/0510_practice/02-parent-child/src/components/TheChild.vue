<template>
  <div class="border-box-red">
    <h2>The Child</h2>
    <input type="text" v-model="childInput" @input="onInput">
    <p>From App => {{ appInput }}</p>
    <p>From Parent => {{ parentInput }}</p>
    <p>From Child => {{ childInput }}</p>
  </div>
</template>

<script>
export default {
  name: 'TheChild',
  props: {
    appInput: String,
    parentInput: String,
  },
  data() {
    return {
      childInput: '',
    }
  },
  methods: {
    onInput() {
      this.$emit('change-child-input', this.childInput)
    }
  }
}
</script>

<style>
  .border-box-red {
    border: 2px solid rgb(233, 41, 41);
    margin: 3px;
  }
</style>