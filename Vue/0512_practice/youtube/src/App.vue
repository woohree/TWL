<template>
  <div id="app">
    <header>
      <search-bar></search-bar> 
    </header>
    <section>
      <movie-detail></movie-detail>
      <movie-list></movie-list>
    </section>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import MovieList from '@/components/MovieList.vue'
import MovieDetail from '@/components/MovieDetail.vue'


export default {
  name: 'App',
  components: {
    SearchBar,
    MovieList,
    MovieDetail,
  },
}
</script>

<style>
  section,
  header {
    width: 80%;
    margin: 0 auto;
    padding: 1rem 0;
  }
  section {
    display: flex;
  }
</style>
