<template>
  <div>
    Todo Form
    <input type="text" @keyup.enter="createTodo" v-model.trim="todoTitle">
  </div>
</template>

<script>

export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: ''
    }
  },
  methods: {
    createTodo() {
      const newTodo = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      this.$store.dispatch('createTodo', newTodo)
      this.todoTitle = ''
    }
  },
}
</script>

<style>

</style>