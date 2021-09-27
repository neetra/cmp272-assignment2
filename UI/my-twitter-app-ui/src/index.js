// Netra
import React, { Component } from 'react';
import { render } from 'react-dom';
import Header from './Header';
import Tweet from './Tweet'
import './style.css';

// Zi
import Form from './Form'

class App extends Component {
  constructor() {
    super();
    this.state = {
      name: 'React'
    };
  }

  render() {
    return (
      <div>
        <Header />
        <Form />               
        <Tweet />
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));
