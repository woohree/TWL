<template>
  <li class="list-group-item" @click="onClick">
    <img :src="videoImgSrc" :alt="video.title">
    {{ video.snippet.title | strUnescape }}
  </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  computed: {
    videoImgSrc() {
      return this.video.snippet.thumbnails.default.url
    },
  },
  filters: {
    strUnescape(rawText) {
      // console.log(rawText.length)
      if (rawText.length > 50) {
        rawText = rawText.slice(0, 50) + '...'
      }
      return _.unescape(rawText)
    },
  },
  methods: {
    onClick() {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>
  .list-group-item {
    display: flex;
    cursor: pointer;
    font-weight: bold;
  }
  .list-group-item:hover {
    background-color: #eee;
  }
  .list-group-item img {
    height: fit-content;
    margin-right: 0.5rem;
  }
</style>