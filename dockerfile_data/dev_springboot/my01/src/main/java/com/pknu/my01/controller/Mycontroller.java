package com.pknu.my01.controller;

import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class Mycontroller {
    @GetMapping("/")
    public String mainPage(Model model) {
        List<String> pageNames = List.of("ex01", "ex02", "ex03", "ex04");
        model.addAttribute("pages", pageNames);
        model.addAttribute("hello", "만나서 아주 반갑습니다. 스프링부트 시작합니다.");
        model.addAttribute("name", "엄보성");
        model.addAttribute("age", 26);
        model.addAttribute("gender", "남");
        return "index";

    }

    @GetMapping("/ex01")
    public String ex01(Model model) {
        model.addAttribute("hello", "만나서 아주 반갑습니다. 스프링부트 시작합니다.");
        model.addAttribute("name", "이성훈");
        model.addAttribute("age", 26);
        model.addAttribute("gender", "남");
        return "ex01";

    }

    @GetMapping("/ex02")
    public String ex02(Model model) {
        List<Integer> sampleNumbers = List.of(1, 2, 3, 4, 5, 6, 7);

        model.addAttribute("numbers", sampleNumbers);
        return "ex02";

    }

}
