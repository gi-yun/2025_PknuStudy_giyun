import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css"; // 이 줄도 중요!

const FetchData = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      fetch("https://jsonplaceholder.typicode.com/posts")
        .then(res => res.json())
        .then(result => {
          setData(result);
          setLoading(false);
        })
        .catch(err => {
          console.log(err);
          setLoading(false);
        });
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      <h1>10. 데이터 가져오기 및 표현</h1>
      {loading ? (
        <div className="d-flex justify-content-center align-items-center" style={{ height: "100px" }}>
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Loading...</span>
          </div>
        </div>
      ) : (
        <ol>
          {data.map((v) => (
            <li key={v.id}>{v.title}</li>
          ))}
        </ol>
      )}
    </>
  );
};

export default FetchData;
