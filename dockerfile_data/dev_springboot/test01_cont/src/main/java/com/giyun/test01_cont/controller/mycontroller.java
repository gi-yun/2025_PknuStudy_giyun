package com.giyun.test01_cont.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
class mycontroller {

    @GetMapping("/api/hello")
    public String hello() {
        return "✅ 스프링에서 온 응답입니다!";
    }

}
