import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';

import {BrowserRouter, Route, Routes, NavLink, useParams, Outlet} from 'react-router-dom'

function Home() {
  return (
    <div>
      <h2>Home</h2>
      Home...
    </div>
  )
}

function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      Contact...
    </div>
  )
}

function NotFound() {
  return (
    <div>
      <h2>404 Not Found</h2>
    </div>
  )
}

function Topic() {
  const params = useParams()
  const topic_id = params.topic_id
  let selected_topic = {
    title: '',
    des: '',
  }
  for (let i=0; i<contents.length; i++) {
    if (contents[i].id === Number(topic_id)) {
      selected_topic = contents[i]
      break
    }
  }
  return (
    <div>
      <h2>{selected_topic.title}</h2>
      {selected_topic.des}
    </div>
  )
}

function Topics() {
  const lis = []
  for (let i=0; i<contents.length; i++) {
    lis.push(<li key={contents[i].id}><NavLink to={"/topics/"+contents[i].id}>{contents[i].title}</NavLink></li>)
  }
  return (
    <div>
      <h2>Topics</h2>
      <ul>
        {lis}
      </ul>
      <Outlet></Outlet>
    </div>
  )
}

const contents = [
  {id: 1, title: 'HTML', des: 'HTML is ...'},
  {id: 2, title: 'JS', des: 'JS is ...'},
  {id: 3, title: 'REACT', des: 'REACT is ...'},
]

function App() {
  return (
    <BrowserRouter>
      <div>
        <h1>Hello React Router DOM</h1>
        <ul>
          <li><NavLink to="/">Home</NavLink></li>
          <li><NavLink to="/topics">Topics</NavLink></li>
          <li><NavLink to="/contact">Contact</NavLink></li>
        </ul>
        <Routes>
          <Route path="/" element={<Home/>}></Route>
          <Route path="/topics" element={<Topics/>}>
            <Route path=":topic_id" element={<Topic/>}></Route>
          </Route>
          <Route path="/contact" element={<Contact/>}></Route>
          <Route path="*" element={<NotFound/>}></Route>
        </Routes>
      </div>
    </BrowserRouter>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
      <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
