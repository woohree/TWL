<template>
  <div class="search-bar" :style="{ margin: isMovies ? '0' : '40vh 0' }">
    <div @click="onClickLogo">
      <span>Welcome</span>
      <span>Woohree</span>
      <span>TMDB Lab</span>
    </div>
    <input id="search" type="text" v-model="keyword" @keydown.enter="fetchMovies(keyword)">
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

// window.addEventListener('keyup', event => {
//   if (event.key === 'Enter') {
//     const search = document.querySelector('#search')
//     search.focus()
//   }
// })

export default {
  name: 'SearchBar',
  data() {
    return {
      keyword: '',
    }
  },
  methods: {
    ...mapActions(['fetchMovies']),
    // fetchMovies(event) {
      //   this.$store.dispatch('fetchMovies', event.target.value)
    // },
    onClickLogo() {
      this.keyword = ''
      this.$store.dispatch('onClickLogo')
    },
  },
  computed: {
    ...mapGetters(['isMovies',])
  }
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