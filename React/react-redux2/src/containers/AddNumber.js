import AddNumber from "../components/AddNumber";
import { connect } from "react-redux";
import store from "../store";


function mapReduxDispatchToReactProps(dispatch) {
  return {
    onClick(size) {
      store.dispatch({type: 'INCREAMENT', size: size})
    }
  }
}

export default connect(null, mapReduxDispatchToReactProps)(AddNumber)


// import React, {Component} from "react";
// import store from '../store'

// export default class extends Component {
//   render() {
//     return <AddNumber onClick={size => {
//       store.dispatch({type: 'INCREAMENT', size: size})
//     }}></AddNumber>
//   }
// }