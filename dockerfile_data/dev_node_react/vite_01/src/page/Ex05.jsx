import { useState } from "react";
import list from "./list.js"; // Assuming list.js exports an array of options

const Radio = () => {
  const [rad, setRad] = useState("");

  const handleRad = (e) => {
    const { value } = e.target;
    setRad(value); // 라디오는 하나만 선택되므로 문자열로 저장
  };

  

  return (
    <>
      <h1>5. 라디오버튼과 확인</h1>
      <h2>선택한 값: {rad}</h2>

      {list.map((v, i) => (
        <div key={i}>
          <input
            type="radio"
            name="one"
            value={v}
            onChange={handleRad}
            checked={rad === v}
          />
          <label>{v}</label>
        </div>
      ))}
    </>
  );
};

export default Radio;
