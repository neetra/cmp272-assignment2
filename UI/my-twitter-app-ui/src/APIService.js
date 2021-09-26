export default class APIService{
  static CreateTweet(status) {
    console.log(status)
    return fetch('http://127.0.0.1:5000/tweet/post/'+status.status,{
      'method':'POST',
      headers : {
        'Content-Type':'application/json'
      }})
    .then(response => response.json())
    .catch(error => console.log(error))
  }

}
