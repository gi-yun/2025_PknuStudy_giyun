const Home = () => {
    return (
        <>
            <h1>1. 라우터 기능 장착</h1>
            <pre><code>
                {`<Link to="/">🏠Home🏠</Link>|{""}
                <Link to="/crypto">Crypto</Link>|{""}
                <Link to="/localstorage">LocalStorage</Link>|{""}
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/crypto" element={<Crypto />} />
                    <Route path="/localstorage" element={<LocalStorage />} />
                </Routes>`}
            </code></pre>
        </>

    )

}
export default Home