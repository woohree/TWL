<template>
  <div>
    <h1>{{ article.title }}</h1>

    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor">
      <button>Edit</button>
      |
      <button>Delete</button>
    </div>

    <!-- Article Like UI -->
    <div>
      Likeit:
      <button @click="likeArticle(articlePk)">{{ article.like_users.length }}</button>
    </div>

    <hr />
    <!-- Comment UI -->
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'ArticleDetail',
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article'])
    },
    methods: {
      ...mapActions(['fetchArticle', 'likeArticle'])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
