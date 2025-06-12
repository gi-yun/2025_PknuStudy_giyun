import { useState } from 'react'
import {Link, Routes, Route} from 'react-router-dom'
import './App.css'
import Home from "./page/Home"
import CSS from "./page/Ex07"
import TodoList from "./page/Ex08"
import Eff from "./page/Ex09"
import FetchData from "./page/Ex10"
import UseM from "./page/Ex11"
import Table from "./page/Ex12"
import Ex12a from "./page/Ex12a"
import Ball from "./page/Ex13"
import Axi from "./page/Ex14"

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Link to="/">Home</Link>|{" "}
      <Link to="/ex07">예제7</Link>|{" "}
      <Link to="/ex08">예제8</Link>|{" "}
      <Link to="/ex09">예제9</Link>|{" "}
      <Link to="/ex10">예제10</Link>|{" "}
      <Link to="/ex11">예제11</Link>|{" "}
      <Link to="/ex12">예제12</Link>|{" "}
      <Link to="/ex12a">예제12a</Link>|{" "}
      <Link to="/ex13">예제13</Link>|{" "}
      <Link to="/ex14">예제14</Link>|{" "}
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/ex07" element={<CSS/>} />
        <Route path="/ex08" element={<TodoList/>} />
        <Route path="/ex09" element={<Eff/>} />
        <Route path="/ex10" element={<FetchData/>} />
        <Route path="/ex11" element={<UseM/>} />
        <Route path="/ex12" element={<Table/>} />
        <Route path="/ex12a" element={<Ex12a/>} />
        <Route path="/ex13" element={<Ball/>} />
        <Route path="/ex14" element={<Axi/>} />
      </Routes>
    </>
  )
}

export default App
