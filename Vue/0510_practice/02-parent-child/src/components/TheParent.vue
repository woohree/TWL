<template>
  <div class="border-box-green">
    <h2>The Parent</h2>
    <input type="text" v-model="parentInput" @input="onInput">
    <p>From App => {{ appInput }}</p>
    <p>From Child => {{ childInput }}</p>
    <the-child :app-input="appInput" :parent-input="parentInput" @change-child-input="getChildInput"></the-child>
  </div>
</template>

<script>
import TheChild from '@/components/TheChild.vue'

export default {
  name: 'TheParent',
  components: {
    TheChild,
  },
  props: {
    appInput: String,
  },
  data() {
    return {
      parentInput: '',
      childInput: '',
    }
  },
  methods: {
    onInput() {
      this.$emit('change-parent-input', this.parentInput)
    },
    getChildInput(childInput) {
      this.childInput = childInput
      this.$emit('change-child-input', childInput)
    }
  }
}
</script>

<style>
  .border-box-green {
    border: 2px solid rgb(50, 224, 65);
    margin: 3px;
  }

</style>