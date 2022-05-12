<template>
  <div>
    <span @click="updateTodoStatus(todo)" :class="{ 'is-completed': todo.isCompleted }">
    {{ todo.title }}
    </span>
    <button @click="deleteTodo(todo)">[x]</button> <!-- ()는 실행이 아니라 넘겨주는 인자를 뜻함 -->
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    ...mapActions(['deleteTodo', 'updateTodoStatus'])
    }
}
</script>

<style scoped>
  .is-completed {
    text-decoration: line-through;
  }
  div {
    border: 2px solid black;
    margin: 2px;
    padding: 2px;
  }
  span {
    cursor: pointer;
  }
</style> 
