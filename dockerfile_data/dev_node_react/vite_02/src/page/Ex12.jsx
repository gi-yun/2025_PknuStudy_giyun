import {useState} from "react";
import data from "./Ex12.data"; // 데이터 import
import tableCss from "./Ex12.module.css"; // CSS 모듈 import


const Table = () => {
    const [ea, setEa] = useState(Array(data.length).fill(1)); // 수량 초기화
    
    const handleNum = (e) => {
        // const index = e.target.id;
        // const value = e.target.value;
        const {index,  value} = e.target; // 이벤트 객체에서 index와 value 추출
        const newEa = [...ea]
        newEa[index] = value; // 해당 인덱스의 수량 업데이트
        setEa(newEa);
    }
  
    return (
  
    <>
    <h1>데이터 임포트 후 실시간 연산</h1>
    {/* {JSON.stringify(data)} */}
    <div className={tableCss["data-box"]}>

        <table border={1}>
            {
                data.map((v,i)=>{
                    return(     
                        <tr key={i}>
                        <td>{v.product_name}</td>
                        <td>{v.price.toLocaleString('ko-KR')}</td>
                        <td>{v.category}</td>
                        <td>{v.delivery_price.toLocaleString('ko-KR')}</td>
                        <td><input id={i}  type="number" onChange={handleNum} value={ea[i]}/></td>
                        <td>{(v.price*ea[i]+(ea[i]>0? v.delivery_price:0)).toLocaleString('ko-KR')}</td>
                    </tr>)
               
            })
        }
            <tr>
                <td colSpan={5}>합계</td>
                <td>{"총합"}</td>

            </tr>
        </table>
        </div>
    </>
  );
};

export default Table;
