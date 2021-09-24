import React, {Component, Fragment} from 'react';
import twittericon from './twitter_icon.png'
class Header extends Component{
  constructor(){
    super()    
  }

  render(){
    return(
      <Fragment>
      <div className = 'header'>
          <img className = 'twitter-icon'src={twittericon} />
          <div className= 'home'>Home</div>
      </div>     
      </Fragment>
    )
  }
}

export default Header;