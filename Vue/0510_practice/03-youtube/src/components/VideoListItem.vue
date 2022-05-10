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
    margin-bottom: 1rem;
    cursor: pointer;
  }
  .list-group-item:hover {
    background-color: #eee;
  }
  .list-group-item img {
    height: fit-content;
    margin-right: 0.5rem;
  }
</style>