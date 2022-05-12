<template>
  <div class="video-detail" v-if="isMovie">
    <div class="video-container">
      <img :src="movieSrc" :alt="movieTitle">
      <div class="video-info">
        <h4>{{ movieTitle | strUnescape }}</h4>
        <p>{{ movieOverview | strUnescape }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex'

export default {
  name: 'MovieDetail',
  computed: {
    ...mapState(['movie',]),
    ...mapGetters(['movieTitle', 'movieSrc', 'movieOverview', 'isMovie',])
  }
}
</script>

<style scoped>
  .video-detail {
    width: 70%;
    padding-right: 2rem;
  }
  .video-container {
    position: relative;
    padding-top: 60%;
  }
  .video-container > img {
    position: absolute;
    top: 0;
    left: 30%;
    width: 40%;
  }
  .video-info {
    margin-top: 20px;
    padding: 20px;
    border: solid 1px lightgray;
    border-radius: 10px;
  }
  .video-info > h4 {
    font-weight: bold;
  }
</style>