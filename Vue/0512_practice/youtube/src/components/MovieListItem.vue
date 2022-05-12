<template>
  <li class="list-group-item" @click="pickMovie(movie)">
    <img :src="movieSrc" :alt="movieTitle">
    <div>
      <h2>{{ movieTitle | strUnescape }}</h2>
      <span>Popularity: {{ movie.popularity | strUnescape }}</span>
      <br>
      <span>Vote Average: {{ movie.vote_average | strUnescape }}</span>
      <br>
      <span>Vote Count: {{ movie.vote_count | strUnescape }}</span>
    </div>
  </li>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'VideoListItem',
  props: {
    movie: Object,
  },
  methods: {
    ...mapActions(['pickMovie',]),
    // pickMovie() {
    //   this.$store.dispatch('pickMovie', this.movie)
    // }
  },
  computed: {
    movieSrc() {
      return 'https://image.tmdb.org/t/p/original' + this.movie.poster_path
    },
    movieTitle() {
      return this.movie.title
    },
  }
}
</script>

<style>
  .list-group-item {
    display: flex;
    cursor: pointer;
    /* font-weight: bold; */
  }
  .list-group-item:hover {
    background-color: #eee;
  }
  .list-group-item img {
    width: 30%;
    margin-right: 0.5rem;
  }
</style>