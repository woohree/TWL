import './App.css';
import React from 'react'
import {useState, useEffect} from 'react'

const funcStyle = 'color: blue'
let funcId = 0
function FuncComp(props) {
  const [number, setNumber] = useState(props.initNumber)
  const [date, setDate] = useState((new Date()).toString())
  
  useEffect(() => {
    console.log('%cfunc => useEffect (componentDidMount) A '+(++funcId), funcStyle)
    document.title = number
    return function() {  // cleanUp
      console.log('%cfunc => useEffect return (componentDidMount) A '+(++funcId), funcStyle)
    }
  }, [])  // 빈 배열을 전달하면, 처음 1회만 실행(부모컴포넌트에서 해당 컴포넌트를 언마운트시킬 때도, componentWillUnmount) / 인자가 없으면 매 랜더마다 실행

  useEffect(() => {
    console.log('%cfunc => useEffect (componentDidMount & componentDidUpdate) A '+(++funcId), funcStyle)
    document.title = number
    return function() {  // cleanUp
      console.log('%cfunc => useEffect return (componentDidMount & componentDidUpdate) A '+(++funcId), funcStyle)
    }
  }, [number])  // number가 변할 때만 useEffect 호출
  // useEffect(() => {
  //   console.log('%cfunc => useEffect (componentDidMount & componentDidUpdate) B '+(++funcId), funcStyle)
  //   document.title = number + ': ' + date
  // })
  console.log('%cfunc => render '+(++funcId), funcStyle)
  return (
  <div className="container">
    <h2>function Style Component</h2>
    <p>Number: {number}</p>
    <p>Date: {date}</p>
    <input type="button" value="random" onClick={() => {
      setNumber(Math.random())
    }}/>
    <input type="button" value="date" onClick={() => {
      setDate((new Date()).toString())
    }}/>
  </div>
  )
}

const classStyle = 'color: red'
class ClassComp extends React.Component{
  state = {
    number: this.props.initNumber,
    date: (new Date()).toString(),
  }
  // static getDerivedStateFromProps() {
  //   console.log('%cclass => getDerivedStateFromProps', classStyle)
  // }
  // componentDidMount() {
  //   console.log('$cclass => componentDidMount', classStyle)
  // }
  render() {
    // console.log('%cclass => render', classStyle)
    return (
      <div className="container">
        <h2>Class Style Component</h2>
        <p>Number: {this.state.number}</p>
        <p>Date: {this.state.date}</p>
        <input type="button" value="random" onClick={() => {
          this.setState({number: Math.random()})
        }}/>
        <input type="button" value="date" onClick={() => {
          this.setState({date: (new Date()).toString()})
        }}/>
      </div>
    )
  }
}

function App() {
  const [funcShow, setFuncShow] = useState(true)
  const [classShow, setClassShow] = useState(true)
  const [funcInputValue, setFuncInputValue] = useState('remove func')
  const [classInputValue, setclassInputValue] = useState('remove class')
  return (
    <div className="container">
      <h1>Hello, Woohree!</h1>
      <input type="button" value={funcInputValue} onClick={(e) => {
        if (funcShow) {
          setFuncShow(false)
          setFuncInputValue('create func')
        } else {
          setFuncShow(true)
          setFuncInputValue('remove func')
        }
      }}/>
      <input type="button" value={classInputValue} onClick={(e) => {
        if (classShow) {
          setClassShow(false)
          setclassInputValue('create class')
        } else {
          setClassShow(true)
          setclassInputValue('remove class')
        }      }}/>
      {funcShow ? <FuncComp initNumber={2}></FuncComp> : null}
      {classShow ? <ClassComp initNumber={2}></ClassComp> : null}
    </div>

  );
}


export default App;
