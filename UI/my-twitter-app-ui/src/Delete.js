export default class Delete{
    static DeleteTweet(status) {
      console.log(status)  
      return fetch('http://127.0.0.1:5000/tweet/delete/'+status.status,{
        'method':'DELETE',
        headers : {
          'Content-Type':'application/json'
        }})
      .then(response => response.json())
      .catch(error => console.log(error))
    }
  
  }