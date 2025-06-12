import { use, useEffect, useState } from 'react'

const Child = () => {
    const [count, setCount] = useState(0);
    const mystyle = {
        border: "2px solid black",
        borderRadius: "10px",
        padding: "1rem",
        backgroundColor: "beige",
        color: "black",
        margin: "10px"
    }
    console.log("1.컴포넌트 함수(Child)가 실행됨")
    let tt = 1
    useEffect(() => {
        console.log("2.컴포넌트가 마운트됨")
        const timer = setInterval(() =>{
            console.log(`3.컴포넌트가 마운트된 상태에서 1초마다 실행됨 ${tt++} 메모리 사용`)
        },1000);
        return () => {
            console.log("4.클린업: 언마운트 또는 업데이트 직전에 청소")
            clearInterval(timer);
        }

    }, [count]);

    return (
        <div style={mystyle}>
            <h2>자식 컴포넌트 테스트</h2>
            <p>자식 컴포넌트의 카운트: {count}</p>
            <button onClick={() => setCount(count + 1)}>+1 카운트 증가</button>
        </div>
    )
}


const Eff = () => {
    const [show, setShow] = useState(true);
    return (
        <>
            <h1>9. useEffect 생명주기 실습</h1>
            <button onClick={() => setShow(!show)}>{show ? '자식 컴포넌트 숨기기' : '자식 컴포넌트 보이기'} </button>
            {show && <Child />}
        </>
    )
}
export default Eff;