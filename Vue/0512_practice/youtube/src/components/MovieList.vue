<template>
  <div class="col">
    <ul class="list-group">
      <movie-list-item v-for="movie in movies" :key="movie.id" :movie="movie"></movie-list-item>
    </ul>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'VideoList',
  components: {
    MovieListItem,
  },
  computed: {
    ...mapState(['movies',]),
  }
}
</script>

<style>

</style>