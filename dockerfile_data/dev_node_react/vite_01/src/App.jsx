import { useState } from 'react'
import { Link, Routes, Route} from 'react-router-dom'
import './App.css'

import Inp from "./page/Ex01"
import Inp2 from "./page/Ex02"
import Inp3 from "./page/Ex03"
import Sel from "./page/Ex04"
import Home from "./page/Home"
import Radio from './page/Ex05'
import Check from './page/Ex06'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Link to="/">Home</Link>|
    <Link to="/ex01">예제1</Link>|
    <Link to="/ex02">예제2</Link>|
    <Link to="/ex03">예제3</Link>|
    <Link to="/ex04">예제4</Link>|
    <Link to="/ex04">예제4</Link>|
    <Link to="/ex05">예제5</Link>|
    <Link to="/ex06">예제6</Link>|
    <Routes>
      <Route path="/" element={<Home/>} ></Route>
      <Route path="/ex01" element={<Inp/>} ></Route>
      <Route path="/ex02" element={<Inp2/>} ></Route>
      <Route path="/ex03" element={<Inp3/>} ></Route>
      <Route path="/ex04" element={<Sel/>} ></Route>
      <Route path="/ex05" element={<Radio/>} ></Route>
      <Route path="/ex06" element={<Check/>} ></Route>
    </Routes>
    </>
  )
}

export default App
