import { useState } from "react";
import list from "./list.js"; // 예: ["사과", "바나나", "포도"]

const Check = () => {
  const [checkedItems, setCheckedItems] = useState([]);

  const handleCheck = (e) => {
    const { value, checked } = e.target;

    if (checked) {
      setCheckedItems((prev) => [...prev, value]);
    } else {
      setCheckedItems((prev) => prev.filter((item) => item !== value));
    }
  };

  return (
    <>
      <h1>6. 체크박스값 확인</h1>
      {list.map((v, i) => (
        <div key={i}>
          <input
            type="checkbox"
            name="one"
            value={v}
            onChange={handleCheck}
            checked={checkedItems.includes(v)}
          />
          <label>{v}</label>
        </div>
      ))}

      <h2>선택한 항목: {checkedItems.join(", ")}</h2>
    </>
  );
};

export default Check;
