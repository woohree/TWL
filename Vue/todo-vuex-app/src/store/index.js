import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [  // localStorage에 state 자동저장
    createPersistedState()
  ],
  state: {  // data
    todos: []
  },
  getters: {  // computed
    // 현재 끝난 일의 개수
    allTodosCount(state) {
      return state.todos.length
    },
    completedTodoCount(state) {
      return state.todos.filter(todo => todo.isCompleted).length
    },
    unCompletedTodoCount(state) {
      return state.todos.filter(todo => !todo.isCompleted).length
    }
  },
  mutations: {  // change!
    // LOAD_TODOS(state) {
    //   const todosString = localStorage.getItem('todos')
    //   state.todos = JSON.parse(todosString)
    // },
    CREATE_TODO(state, newTodo) {
      state.todos.push(newTodo)
    },
    DELETE_TODO(state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
    UPDATE_TODO_STATUS(state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          todo.isCompleted = !todo.isCompleted
        }
        return todo
      })
    },
  },
  actions: {  // methods
    // saveTodos({ state }) {
    //   const jsonData = JSON.stringify(state.todos)
    //   localStorage.setItem('todos', jsonData)
    // },
    createTodo(context, newTodo) { // const { commit } = context
      context.commit('CREATE_TODO', newTodo)
      // context.dispatch('saveTodos')      
    },
    deleteTodo({ commit }, todoItem) {
      if (confirm('진짜임?')) {
        commit('DELETE_TODO', todoItem)
        // dispatch('saveTodos')
      }
    },
    updateTodoStatus({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
      // dispatch('saveTodos')
    }
  },
})
