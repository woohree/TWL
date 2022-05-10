<template>
  <div class="col">
    <ul class="list-group">
      <video-list-item 
      v-for="video in videos" 
      :key="video.id.videoId" 
      :video="video"
      @select-video="onSelectVideo"></video-list-item>
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: { VideoListItem },
  props: {
    videos: Array,
  },
  methods: {
    onSelectVideo(video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>