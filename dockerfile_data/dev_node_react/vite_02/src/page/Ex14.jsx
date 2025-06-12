import { useState } from "react"
import axios from 'axios'
const url = "https://api.thecatapi.com/v1/images/search?limit=10"

const Axi = () => {
  const [sdata, setSdata] = useState({ username: "", password: "" })
  const [mydata, setMydata] = useState('')
  const [odata, setOdata] = useState('')

  const handleInput = e => {
    setSdata(pre => ({ ...pre, [e.target.name]: e.target.value }))
  }

  const sendPost = () => axios.post('/data', sdata).then((res) => console.log(res.data))

  const myApi = () => axios.get('/api').then(res => setMydata(res.data))
  const catapi = () => axios.get(url).then(res => setOdata(res.data))

  return (
    <>
      <h1>14. AXIOS로 데이터 통신</h1>

      <div>
        <h2>서버로 보내는 값</h2>
        ID: <input type="text" name="username" onChange={handleInput} value={sdata.username} />{" "} <br />
        PW: <input type="password" name="password" onChange={handleInput} value={sdata.password} />{" "}
        <button onClick={sendPost}>전송</button>
        <div>id: {sdata.username} / pw: {sdata.password}</div>
      </div>

      <hr />

      <button onClick={myApi}>내 서버에서 수신</button>
      <div>내 서버에서 받은 값</div>
      <div>{mydata}</div>

      <hr />

      <button onClick={catapi}>외부 서버에서 수신</button>
      <div>외부 서버에서 받은 값</div>
      <div>{}</div>
    </>
  );
};

export default Axi;
