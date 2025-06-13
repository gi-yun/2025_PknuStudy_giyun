import { useState } from "react"
import axios from 'axios'
import './App.css'

const App = () => {
  const [sdata, setSdata] = useState({ name: "", age: "", memo: "" })
  const [listData, setListData] = useState([])
  const [apiData, setApiData] = useState(null)

  const handleInput = e => {
    setSdata(prev => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const sendPost = () => {
    axios.post('/data', sdata)
      .then(res => console.log("데이터 전송 완료:", res.data))
  }

  const getApiData = () => {
    axios.get('/api')
      .then(res => {
        console.log("서버에서 받은 저장 데이터:", res.data)
        setApiData(res.data.data)
      })
      .catch(err => console.error("API 요청 에러", err))
  }

  const list = () => {
    axios.get('/list')
      .then(res => setListData(res.data))
      .catch(err => console.error("리스트 요청 에러", err))
  }

  return (
    <div style={{
      fontFamily: "Arial, sans-serif",
      padding: "20px",
      maxWidth: "800px",
      margin: "0 auto",
      boxSizing: "border-box"
    }}>
      <h1 style={{ textAlign: "center" }}>AXIOS로 데이터 통신</h1>

      {/* 입력 폼 */}
      <div style={{
        display: "flex",
        flexDirection: "column",
        gap: "10px",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
        backgroundColor: "#f5f5f5",
        marginBottom: "20px"
      }}>
        <h2>서버로 보내는 값</h2>
        <input type="text" name="name" onChange={handleInput} value={sdata.name} placeholder="이름 입력" />
        <input type="text" name="age" onChange={handleInput} value={sdata.age} placeholder="나이 입력" />
        <input type="text" name="memo" onChange={handleInput} value={sdata.memo} placeholder="메모 입력" />
        <button onClick={sendPost} style={{ padding: "10px", fontWeight: "bold" }}>전송</button>

        {/* 응답 출력 박스 */}
        {(sdata.name || sdata.age || sdata.memo) && (
          <div style={{
            marginTop: "10px",
            padding: "10px",
            border: "1px solid #ddd",
            borderRadius: "8px",
            backgroundColor: "#fff"
          }}>
            {sdata.name && <p><strong>이름:</strong> {sdata.name}님</p>}
            {sdata.age && <p><strong>나이:</strong> {Number(sdata.age) + 1}세 (+1세 처리됨)</p>}
            {sdata.memo && <p><strong>메모:</strong> {sdata.memo} 라고 잘 받았습니다.</p>}
          </div>
        )}
      </div>

      {/* /api 응답 보기 */}
      <div style={{
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
        backgroundColor: "#eef7ff",
        marginBottom: "20px"
      }}>
        <h2>/api 요청으로 저장된 데이터 가져오기</h2>
        <button onClick={getApiData} style={{ padding: "10px", fontWeight: "bold", marginBottom: "10px" }}>저장된 데이터 가져오기</button>
        {apiData && (
          <div style={{
            padding: "10px",
            backgroundColor: "#fff",
            borderRadius: "8px",
            border: "1px solid #ddd"
          }}>
            <p><strong>이름:</strong> {apiData.name}</p>
            <p><strong>나이:</strong> {apiData.age}</p>
            <p><strong>메모:</strong> {apiData.memo}</p>
          </div>
        )}
      </div>

      {/* /list 과일 리스트 출력 */}
      <div style={{
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "10px",
        backgroundColor: "#f9f9f9"
      }}>
        <h2>/list 요청해서 받은 과일 목록</h2>
        <button onClick={list} style={{ padding: "10px", fontWeight: "bold", marginBottom: "10px" }}>과일 목록 가져오기</button>
        <div style={{
          backgroundColor: "#fff",
          padding: "10px",
          borderRadius: "8px",
          border: "1px solid #ddd",
          whiteSpace: "pre-wrap",
          wordBreak: "break-word"
        }}>
         {JSON.stringify(listData)}
        </div>
      </div>
    </div>
  )
}

export default App
