// import React from "react"
import { useState, useEffect } from "react"

const Inp2= () => {
    const [theme, setTheme] = useState(()=>{
        return localStorage.getItem('theme') || 'light'
    })

    useEffect(() => {
        localStorage.setItem('theme', theme)
    }, [theme])
const toggle =() => {
    setTheme( th => th==="light" ? "dark" :"light")
}
    
    return(
        <>
        {/* div.dark-mode>h1+button */}
        <div className={theme == 'light' ? 'light-mode' : 'dark-mode'}>
            <h1>{theme == 'light' ? '☀️주간모드' : '🌆야간모드'}</h1>
            <button onClick={toggle} >테마 변경</button>
        </div>
        </>
    )
}
export default Inp2