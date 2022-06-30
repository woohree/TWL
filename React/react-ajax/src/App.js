import React, { Component } from 'react'


class Nav extends Component {
  render() {
    let listTag = []
    for (let i=0; i<this.props.list.length; i++) {
      let li = this.props.list[i]
      listTag.push(<li key={li.id}><a href={li.id} data-id={li.id} onClick={e => {
        e.preventDefault()
        this.props.onClick(e.target.dataset.id)
      }}>{li.title}</a></li>)
    }
    return (
      <nav>
        <ul>
          {listTag}
        </ul>
      </nav>
    )
  }
}

class Article extends Component {
  render() {
    return (
      <article>
        <h2>{this.props.title}</h2>
        {this.props.desc}
      </article>
    )
  }
}

class NowLoading extends Component {
  render() {
    return <div>Now Loading...</div>
  }
}

class App extends Component {
  state = {
    article: {
      item: {
        title: "Welcome",
        desc: "Hellod, React & Ajax",
      },
      isLoading: false,
    },
    list: {
      items: [],
      isLoading: false,
    }
  }

  componentDidMount() {
    let newList = Object.assign({}, this.state.list, {isLoading: true})
    this.setState({list: newList})
    fetch('list.json')
      .then(res => {
        return res.json()
      })
      .then(json => {
        // console.log(json)
        this.setState({list: {
          items: json,
          isLoading: false,
        }})
      })
  }

  render() {
    let NavTag = null
    if (this.state.list.isLoading) {
      NavTag = <NowLoading></NowLoading>
    } else {
      NavTag = <Nav list={this.state.list.items} onClick={id => {
        let newArticle = Object.assign({}, this.state.article, {isLoading: true})
        this.setState({article: newArticle})
        fetch(id+'.json')
          .then(res => {
            return res.json()
          })
          .then(json => {
            this.setState({article: {
              item: {
                title: json.title,
                desc: json.desc,
              },
              isLoading: false,
            }})
          })
      }}></Nav>
    }

    let ArticleTag = null
    if (this.state.article.isLoading) {
      ArticleTag = <NowLoading></NowLoading>
    } else {
      ArticleTag = <Article title={this.state.article.item.title} desc={this.state.article.item.desc}></Article>
    }
    return (
      <div className="App">
        <h1>WEB</h1>
        {NavTag}
        {ArticleTag}
      </div>
    );
  }
}

export default App;
