<template>
  <div>
    <h1>Pick {{ count }} Lotto</h1>
    <div>
      <h2>{{ luckyNumbers }}</h2>
      <button @click="pickLotto">위이이잉..!</button>
    </div>
    <p>/lotto/6 => 6개 뽑기,
      /lotto/7 => 7개 뽑기
    </p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'LottoView',
  data() {
    return {
      count: this.$route.params.count,
      luckyNumbers: []  
    }
  },
  methods: {
    pickLotto() {
      this.luckyNumbers = _.sampleSize(_.range(1, 46), this.count)
    }
  },
  created() {
    this.pickLotto()
  }
}
</script>

<style>

</style>