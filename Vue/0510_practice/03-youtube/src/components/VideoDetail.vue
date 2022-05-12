<template>
  <div class="video-detail" v-if="isVideo">
    <div class="video-container">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
    <div class="video-info">
      <h4>{{ video.snippet.title | strUnescape }}</h4>
      <p>{{ video.snippet.description | strUnescape }}</p>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoSrc() {
      const videoId = this.video.id?.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
    isVideo() {
      return !_.isEmpty(this.video)
    }
  },
  filters: {
    strUnescape(rawText) {
      return _.unescape(rawText)
    },
  },
}
</script>

<style>
  .video-detail {
    width: 75%;
    padding-right: 2rem;
  }
  .video-container {
    position: relative;
    padding-top: 56.28%;
  }
  .video-container > iframe {
    position: absolute;
    top: 0;
    width: 100%;
    height: 100%;
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