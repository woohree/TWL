<template>
  <div class="search-bar" :style="{ margin: isVideos ? '0' : '40vh 0' }">
    <input type="text" @keyup.enter="onEnter" placeholder="Search">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  props: {
    isVideos: Boolean,
  },
  methods: {
    onEnter(event) {
      this.$emit('search-keyword', event.target.value)
    },
  },
}
</script>

<style>
  .search-bar > input {
    width: 100%;
    padding: 0.5rem;
    font-size: 3rem;
  }

  .search-bar {
    transition: margin 1s;
  }
</style>