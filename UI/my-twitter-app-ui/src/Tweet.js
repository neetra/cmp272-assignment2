// Netra:  Container for all Tweets
import React, {Component, Fragment} from 'react';
import deleticon from './delete-icon.png'

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
        
        let tweets = data.map(tweets => {             
              return(              
                <div className='tweet-whole' key = {tweets.id}>  
                <div className = 'title-root'>
                    <div className='title'>{tweets.author}</div>
                    <img className='delete-icon' src={deleticon}></img>
                </div>
                <div className='tweet-text'>
                    {tweets.text}
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