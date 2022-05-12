import _ from 'lodash'
import Vue from 'vue'
import App from './App.vue'
import store from './store'

Vue.config.productionTip = false

Vue.filter('strUnescape', rawText => _.unescape(rawText))


new Vue({
  store,
  render: h => h(App)
}).$mount('#app')


const search = document.querySelector('#search')
window.addEventListener('keyup', event => {
  if (event.key === 'Enter') {
    search.focus()
  }
})
