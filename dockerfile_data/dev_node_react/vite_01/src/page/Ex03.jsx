import { useState } from "react";


const Inp3 = () => {

    const [in1, SetIn1] = useState(0);
    const [in2, SetIn2] = useState(0);

    const handleIn1 = (e) => SetIn1(Number(e.target.value));
    const handleIn2 = (e) => SetIn2(Number(e.target.value));
    console.log(typeof in1, typeof in2)
    return(
        <>
            <h1>1. Input을 이용한 실시간 계산</h1>
            <div>
                <input type="text"  placeholder={in1} onChange={handleIn1}/>+{""}
                <input type="text" placeholder={in1}  onChange={handleIn2} />={in1 + in2}
            </div>

            <div>
                <input type="text" placeholder={in1} onChange={handleIn1}/>-{""}
                <input type="text" placeholder={in1} onChange={handleIn2} />={in1 - in2}
            </div>

            <div>
                <input type="text" placeholder={in1}  onChange={handleIn1}/>*{""}
                <input type="text" placeholder={in1}  onChange={handleIn2} />={in1 * in2}
            </div>

            <div>
                <input type="text" placeholder={in1} onChange={handleIn1}/>/{""}
                <input type="text" placeholder={in2} onChange={handleIn2} />={in1 / in2}
            </div>
        </>
    )
}
export default Inp3;