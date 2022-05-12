import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

Vue.use(Vuex)

// const API_URL = 'https://www.googleapis.com/youtube/v3/search'
// const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://api.themoviedb.org/3/search/movie'
const API_KEY = process.env.VUE_APP_TMDB_API_KEY


export default new Vuex.Store({
  state: {
    keyword: '',
    movies: [],
    movie: {},
    isLoading: false,
  },
  getters: {
    movieTitle: state => state.movie.title ,
    movieSrc: state => 'https://image.tmdb.org/t/p/original' + state.movie.poster_path,
    movieOverview: state => state.movie.overview,
    isMovie: state => !_.isEmpty(state.movie),
    isMovies: state => !!state.movies.length,
  },
  mutations: {
    FETCH_MOVIES(state, movies) {
      state.movies = movies
      state.movie = movies[0]
    },
    PICK_MOVIE: (state, movie) => state.movie = movie,
    ON_CLICK_LOGO(state) {
      state.movies = []
      state.movie = {}

      // Fade-out 함수 ㅋㅋ 
      // let opacity = 0
      // let intervalID = 0
      // function hide(){
      //   const section = document.querySelector("section");
      //   opacity = Number(window.getComputedStyle(section).getPropertyValue("opacity"))
        
      //   if(opacity>0){
      //     opacity -= 0.1
      //     section.style.opacity = opacity
      //   }
      //   else{
      //     clearInterval(intervalID)
      //   }
      // }

      // intervalID = setInterval(hide,50)
    }
  },
  actions: { // mutation에는 비동기 식이 들어가면 안되므로, axios 요청은 actions에서!
    fetchMovies({ state, commit }, keyword) {
      state.isLoading = true
      state.keyword = keyword
      const params = {
        api_key: API_KEY,
        query: keyword,
      }
      axios.get(API_URL, { params })
        .then( res => {

          commit('FETCH_MOVIES', res.data.results)

          
          state.isLoading = false
        })
        .catch(err => console.error(err))
    },
    pickMovie({ commit }, movie) {
      commit('PICK_MOVIE', movie)
    },
    onClickLogo({ commit }) {
      commit('ON_CLICK_LOGO')
    }
  },
  modules: {
  }
})
