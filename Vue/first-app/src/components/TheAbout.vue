<template>
  <!-- 템플릿 안에는 반드시 하나의 element만 있어야 한다. -->
  <div>
    <h1>{{ myMessage }}</h1>
    <p>div 하나에 묶자!!</p>
    <input type="text" v-model='childInputData' @keyup.enter='childInputChange'>
  </div>
</template>

<script>
export default {
  name: 'TheAbout',
  props: {
    myMessage: String,
  },
  data() {
    return {
      childInputData: '들리냐고'
    }
  },
  methods: {
    childInputChange() {
      console.log('child', this.childInputData)
      // 부모 컴포넌트에게 {$emit('이름')} '이름'라는 이름의 이벤트를 발생
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>

</style>