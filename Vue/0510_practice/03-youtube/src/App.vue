<template>
  <div>
    <header>
      <search-bar :is-videos="!!videos.length" @search-keyword="fetchVideos"></search-bar>
    </header>
    <section>
      <video-detail :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="setVideo"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data() {
    return {
      keyword: '',
      videos: [],
      selectedVideo: {},
    }
  },
  methods: {
    fetchVideos(keyword) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: keyword,
      }

      this.keyword = keyword

      axios.get(API_URL, { params })
        .then(res => {
          this.videos = res.data.items
          this.selectedVideo = res.data.items[0]
    })
        .catch(err => console.error(err))
    },
    setVideo(video) {
      this.selectedVideo = video
      console.log(video)
    }
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