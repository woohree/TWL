import {legacy_createStore as createStore} from 'redux'

export default createStore((state, action) => {
  if (state === undefined) {
    return {number: 0}
  }
  
  if(action.type === 'INCREAMENT') {
    return {...state, number: state.number + action.size}
  }
  return state
}, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)