import { useState } from 'react';
import APIService from './APIService'

const Form = (progs) => {
  const [status, setStatus] = useState('')

  const createTweet = () =>{
    APIService.CreateTweet({status})
    .then((response) => console.log(response))
    .then((response) => window.location.reload())
    .catch(error => console.log('error',error))
  }

  const handleSubmit = (event) =>{
    event.preventDefault()
    createTweet()
    setStatus('')
  }

  return (
    <div>
      <form onSubmit = {handleSubmit} >
        <label htmlFor="status" className="form-label">What's up
        </label> <div>
        <textarea
        className="form-control"
        placholder="same something"
        rows='3'
        value={status}
        onChange={(e)=>setStatus(e.target.value)}
        required
        ></textarea> </div>
        <button className="btn btn-primary mt-2">+Tweet</button>
      </form>
    </div>
  )
}


export default Form;
