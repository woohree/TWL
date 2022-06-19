<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input type="text" id="title" />
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea type="text" id="content"></textarea>
    </div>
    <div>
      <button></button>
    </div>
  </form>
</template>

<script>
  // import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {}
    },

    methods: {
      onSubmit() {},
    },
  }
</script>

<style></style>
