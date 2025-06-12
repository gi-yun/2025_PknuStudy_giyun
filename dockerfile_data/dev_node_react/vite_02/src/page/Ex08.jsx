import {useState} from "react"
const TodoList = () => {

    const [indata, setIndata] = useState("");
    const [arr, setArr] = useState([])

    const handleInput =(e) => {
        setIndata(e.target.value)
    }
    const handleAdd = () => {
        setArr([...arr, indata])

    }

    return(
        <>
        <h1>8. 어레이를 이용한 toDoList</h1>
        <label htmlFor="inin">배열요소 입력: </label>
        <input type="text" id="inin"  onChange={handleInput} value={indata}/>
        <button onClick={handleAdd}>추가</button>
        <button >제거</button>
        <div>{indata}</div>
        <hr />
        {/* <div>{arr}</div> */}
        {arr.map((v,i)=>{
            return(
                <div key={i+1}>{`${i+1}: ${v}`}</div>
            )
        })}
        </>
    )
}
export default TodoList;