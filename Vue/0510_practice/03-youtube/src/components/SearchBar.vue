<template>
  <div class="search-bar" :style="{ margin: isVideos ? '0' : '40vh 0' }">
    <div @click="onClickLogo">
      <span>Welcome</span>
      <span>Woohree's</span>
      <span>Youtube Lab</span>
    </div>
    <input type="text" @keyup.enter="onEnter" placeholder="Search">
  </div>
</template>

<script>
window.addEventListener('keyup', event => {
  if (event.key === 'Enter' | event.keyCode === 27) {
    const input = document.querySelector('input')
    console.log(input)
    input.focus()
  }
})


export default {
  name: 'SearchBar',
  props: {
    isVideos: Boolean,
  },
  methods: {
    onEnter(event) {
      this.$emit('search-keyword', event.target.value)
    },
    onClickLogo() {
      const input = document.querySelector('input')
      this.$emit('re-search', input)
    }
  },
}
</script>

<style>
  .search-bar > input {
    width: 100%;
    padding: 0.5rem;
    font-size: 1rem;
    border: 1px solid rgb(218, 41, 41);
    border-radius: 5px;
  }

  .search-bar > input:focus {
    outline: 1px solid rgb(255, 0, 0);
  }

  .search-bar > div {
    display: flex;
    width: 5%;
    flex-direction: column;
    cursor: pointer;
  }

  .search-bar span {
    font-size: 0.7rem;
    font-style: italic;
    color: rgb(226, 31, 31);
  }

  .search-bar {
    transition: margin 1s;
    display: flex;
  }
</style>