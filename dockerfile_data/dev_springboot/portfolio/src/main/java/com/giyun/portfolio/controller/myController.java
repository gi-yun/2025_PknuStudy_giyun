package com.giyun.portfolio.controller;

import org.springframework.stereotype.Controller;
// import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class myController {
    @GetMapping("/")
    public String index() {
        return "forward:/index.html"; // 🔥 dist/index.html 정적 리디렉션
    }

}
