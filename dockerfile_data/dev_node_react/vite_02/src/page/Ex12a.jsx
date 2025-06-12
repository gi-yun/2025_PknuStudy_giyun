import React from "react";
import table from "./Ex12.data"; // 데이터 import
import styles from "./Ex12.module.css"; // CSS 모듈 import

const Ex12a = () => {
  return (
  
    <>
    <h1>12. 데이터 임포트 후 실시간 연산</h1>
    <div className={styles["data-box"]}>
      <table>
        <thead>
          <tr>
            <td>상품명</td>
            <td>가격</td>
            <td>카테고리</td>
            <td>배송비</td>
            <td>수량</td>
            <td>합계</td>
          </tr>
        </thead>
        <tbody>
          {table.map((item, idx) => (
            <tr key={idx}>
              <td>{item.product_name}</td>
              <td>{item.price.toLocaleString()}원</td>
              <td>{item.category}</td>
              <td>{item.delivery_price.toLocaleString()}원</td>
              <td>
                <input type="number" min="1" defaultValue={1} />
              </td>
              <td>
                {/* 단순히 수량 1 기준 합계 표시 */}
                {(item.price + item.delivery_price).toLocaleString()}원
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </>
  );
};

export default Ex12a;
