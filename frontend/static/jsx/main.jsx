import React from 'react'
import axios from 'axios'

var Users = React.createClass({
  getInitialState() {
    return {
      users: [],
    }
  },
  componentWillMount() {
    axios.get('/api/users/', {
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
    })
    .then((response) => {
      this.setState({
        users: response.data,
      })
    })
  },
  renderUser(user) {
    return (
      <div key={user.id} className="user">
        <h2>{user.username}</h2>
        {user.email}
      </div>
    )
  },
  render() {
    return (
      <div className="users">
        <h1>Users</h1>
        {this.state.users.map(this.renderUser)}
      </div>
    )
  },
})

React.render(<Users />, document.body)
