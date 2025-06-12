const Inp= () => {
    const data= {id:1, name:"홍길동", comment:"아버지를 부르지 못하고"}
    const jdata= JSON.stringify(data)
    localStorage.setItem('test3', jdata)
    // Read 읽기
    const readData = localStorage.getItem('test3')
    const oData = JSON.parse(readData)
    // 삭제하기
    localStorage.removeItem('test3')
    // 모두 삭제
    localStorage.clear()
    
    return(
        <>
        <h1>불러왔습니다. {readData}</h1>
        <h2>{oData.name}</h2>
        <h2>{oData.comment}</h2>
        </>
    )
}
export default Inp