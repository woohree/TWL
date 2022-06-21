import './App.css';
import { useState } from 'react'

function Header(props) {
  return <h1><a href="/index" onClick={e => {
    e.preventDefault()
    props.onChangeMode()
  }}>{props.title}</a></h1>
}

function Nav(props) {
  const lis = []
  for (let i=0; i<props.topics.length; i++) {
    const temp = props.topics[i]
    lis.push(<li key={temp.id}><a id={temp.id} href={'/read/'+temp.id} onClick={e => {
      e.preventDefault()
      // console.log(typeof(e.target.id)) // => 문자열, 그러므로 이걸 쓰려면 Number함수를 써서 숫자로 바꿔줘야함
      // props.onChangeMode(Number(e.target.id))
      props.onChangeMode(temp.id)
    }}>{temp.title}</a></li>)
  }
  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}

function Article(props) {
  return <article>
    <h2>{props.title}</h2>
    <p>{props.body}</p>
  </article>
}

function Create(props) {
  return <article>
    <h2>Create</h2>
    <form onSubmit={e => {
      e.preventDefault()
      const title = e.target.title.value
      const body = e.target.body.value
      props.onCreate(title, body)
    }}>
      <p><input type="text" name="title" placeholder='title' /></p>
      <p><textarea name="body" placeholder='body'></textarea></p>
      <p><input type="submit" value="Create" /></p>
    </form>
  </article>
}

function Update(props) {
  const [title, setTitle] = useState(props.title)
  const [body, setBody] = useState(props.body)
  return <article>
    <h2>Update</h2>
    <form onSubmit={e => {
      e.preventDefault()
      const title = e.target.title.value
      const body = e.target.body.value
      props.onUpdate(title, body)
    }}>
      <p><input type="text" name="title" placeholder='title' value={title} onChange={e => {
        setTitle(e.target.value)
      }}/></p>
      <p><textarea name="body" placeholder='body' value={body} onChange={e => {
        setBody(e.target.value)
      }}></textarea></p>
      <p><input type="submit" value="Update" /></p>
    </form>
  </article>
}

function App() {
  const [mode, setMode] = useState('HOME')
  const [id, setId] = useState(null)
  const [nextId, setNextId] = useState(4)
  const [topics, setTopics] = useState([
    {id: 1, title: 'woohree', body: 'GOAT woohree'},
    {id: 2, title: 'tevem', body: 'chobo tevem'},
    {id: 3, title: 'qogksqls', body: 'KIN qogksqls'},
  ])
  let content = ''
  let context = ''

  if (mode === 'HOME') {
    content = <Article title="HOME" body="Hello, SUPER FE DEVELOPER!"></Article>
  } 
  
  else if (mode === 'READ') {
    let title = ''
    let body = ''
    for (let i=0; i<topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title
        body = topics[i].body
      }
    }
    content = <Article title={title} body={body}></Article>
    context = <>
    <li><a href={'/update/'+id} onClick={e => {
      e.preventDefault()
      setMode('UPDATE')
    }}>Update</a></li>
    <li><input type="button" value="Delete" onClick={e => {
      const newTopics = topics.filter(topic => {
        return topic.id !== id
      })
      setTopics(newTopics)
      setMode('HOME')
    }}/></li>
    </>
  } 
  
  else if (mode === 'CREATE') {
    content = <Create onCreate={(title, body) => {
      const newTopic = {
        title: title,
        body: body,
        id: nextId
      }
      const newTopics = [...topics]
      newTopics.push(newTopic)
      setTopics(newTopics)
      setId(nextId)
      setNextId(nextId+1)
      setMode('READ')
    }}></Create>
  }

  else if (mode === 'UPDATE') {
    let title = ''
    let body = ''
    for (let i=0; i<topics.length; i++) {
      if (topics[i].id === id) {
        title = topics[i].title
        body = topics[i].body
        break
      }
    }
    content = <Update title={title} body={body} onUpdate={(title, body) => {
      const updatedTopic = {
        title: title,
        body: body,
        id: id
      }
      const newTopics = [...topics]
      for (let i=0; i<newTopics.length; i++) {
        if (newTopics[i].id === id) {
          newTopics[i] = updatedTopic
          break
        }
      }
      setTopics(newTopics)
      setMode('READ')
    }}></Update>
  }  

  return (
    <div>
      <Header title="HOME" onChangeMode={() => {
        setMode('HOME')
      }}></Header>
      <Nav topics={topics} onChangeMode={id => {
        setId(id)
        setMode('READ')
      }}></Nav>
      {content}
      <ul>
        <li><a href="/create" onClick={e => {
          e.preventDefault()
          setMode('CREATE')
        }}>Create</a></li>
        {context}
      </ul>
    </div>
  );
}

export default App;
