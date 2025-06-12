// // 일반 CSS
// import ".Ex07.css";

// // CSS Module
// import myStyle2 from ".Ex07.module.css";

const CSS = () => {
    const myStyle1 = {
        width: "200px",
        height: "200px",
        borderRadius: "50%",
        backgroundColor: "Green",
    }

    return(
        <>
        <h1>7. 리액트에 CSS 스타일 적용하기</h1>

        <div style={myStyle1}>배고파</div>
        <div style={ {...myStyle1, backgroundColor: "blue",color:"white" }}>배안고파</div>
        {/* <div className="ex7-div">aa</div> */}
        {/* <div className={myStyle2["ex7-div"]}>aa</div> */}
        </>
    )
    }
export default CSS;