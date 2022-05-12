<template>
  <div>
    <todo-list-item v-for="todo in todos" :key="todo.date" :todo="todo"></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
import { mapState } from 'vuex'

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    ...mapState(['todos',])
    // 같은 뜻 
    // todos() {
    //   return this.$store.state.todos
    // },
  }
}
</script>

<style>

</style>