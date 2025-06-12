import { useState, useMemo } from "react";

const ShowState = ({ number, text }) => {
  const heavyCalc = () => {
    let s = 0;
    for (let i = 0; i < 500 * 1000 * 1000; i++) {
      s += i;
    }
    return s;
  };

  // number가 바뀔 때만 무거운 계산 수행
  const calcResult = useMemo(() => heavyCalc(), [number]);

  return (
    <div>
      <h3>무거운 계산 결과: {calcResult}</h3>
      <h2>숫자: {number}</h2>
      <h2>글자: {text}</h2>
    </div>
  );
};

const UseM = () => {
  const [number, setNumber] = useState(0);
  const [text, setText] = useState("");

  return (
    <>
      <h1>11. useMemo 실습 : 렌더링 최적화</h1>
      <h2>숫자변경</h2>
      <button onClick={() => setNumber(number + 1)}>+ 증가</button>
      <button onClick={() => setNumber(number - 1)}>- 감소</button>
      <hr />
      <h2>글자변경</h2>
      <input
        type="text"
        onChange={(e) => setText(e.target.value)}
        value={text}
      />
      <ShowState number={number} text={text} />
    </>
  );
};

export default UseM;
