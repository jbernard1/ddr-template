import React from 'react'
import axios from 'axios'

var Users = React.createClass({
  getInitialState() {
    return {
      users: [],
    }
  },
  componentWillMount() {
    axios.get({
      url: '/api/users/',
      xsrfCookieName: 'csrftoken',
    })
    .then((response) => {
      this.setState({
        users: response.data,
      })
    })
  },
  renderUser(user) {
    return (
      <div className="user">
        <strong>{user.username}</strong>
        {user.email}
      </div>
    )
  },
  render() {
    return (
      <div className="users">
        <h1>Users</h1>
        {this.state.map(this.renderUser)}
      </div>
    )
  },
})

React.render(<Users />, document.body)
