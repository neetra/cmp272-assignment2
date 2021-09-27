// Netra:  Container for all Tweets
import React, {Component, Fragment} from 'react';
import deleticon from './delete-icon.png'
import Delete from './Delete'
class Tweet extends Component {
  constructor(props){
    super(props);
    this.state = {
      tweets: []
    }

    // URL for twitter API
    this.baseURL = "http://127.0.0.1:5000/"
  }

  componentDidMount(){
    fetch(this.baseURL +  'tweets')
      .then(res => res.json())
      .then(data => {

        let tweets = data.map(tweet => {
              return(
                <div className='tweet-whole' key = {tweet.id}>
                <div className = 'title-root'>
                    <div className='title'>{tweet.author}</div>
                   <img className='delete-icon' src={deleticon} title={tweet}
                      onClick={() => Delete.DeleteTweet(tweet.id)}></img>
                </div>
                <div className='tweet-text'>
                    {tweet.text}
                </div>
                </div>
                )
               })
          this.setState({
            tweets: tweets
          })
          console.log(`Data Is ${tweets}`);
      })
  }

  render(){
  return(
    <Fragment>
        <div className = "post">
          {this.state.tweets}
        </div>
    </ Fragment>
  )
  }
}

export default Tweet;
