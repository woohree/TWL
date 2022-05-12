<template>
  <div id="app">
    <h1>My TODOs</h1>
    <h2>전체: {{ allTodosCount }}</h2>
    <h2>완료: {{ completedTodoCount }}</h2>
    <h2>하는중: {{ unCompletedTodoCount }}</h2>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'
import { mapGetters } from 'vuex'
// import { mapGetters, mapMutations } from 'vuex'


export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  computed: {
    ...mapGetters(['completedTodoCount', 'unCompletedTodoCount', 'allTodosCount'])
  },
  // methods: {
  //   ...mapMutations(['LOAD_TODOS'])
  // },
  // created() {
  //   this.LOAD_TODOS()
  // }
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
