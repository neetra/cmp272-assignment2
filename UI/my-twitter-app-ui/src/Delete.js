export default class Delete{
    static DeleteTweet(status) {
      console.log(status)
      return fetch('http://127.0.0.1:5000/tweet/delete/'+status,{
        'method':'POST',
        headers : {
          'Content-Type':'application/json'
        }})
      .then(response => response.json())
    //  .then(window.location.reload())
      .catch(error => console.log(error))
    }

  }
