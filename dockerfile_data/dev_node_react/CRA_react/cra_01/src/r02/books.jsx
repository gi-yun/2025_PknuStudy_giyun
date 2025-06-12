const books = [
    { id: 101, bookname: "세상에 모든 음식", price: 13000 },
    { id: 102, bookname: "자바 잘하는법", price: 30000 },
    { id: 103, bookname: "잠 잘자는법법", price: 23000 },
    { id: 104, bookname: "돈 잘 세는 법법", price: 3000 },
    { id: 105, bookname: "절망", price: 50000 },

]

const Books = () => {
    return (
        <>
            <ul>
                {books.map(v => <li key={v.id}>{v.bookname}({v.price})원</li>)}
            </ul>
        </>
    )
}

export default Books