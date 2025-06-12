package com.pknu.my01_1.controller;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

import com.pknu.my01_1.dto.BungBbang;
import com.pknu.my01_1.dto.MemberData;

@Controller
public class My01Controller {
    @GetMapping("/")
    public String mainPage(Model model) {
        return "main"; // templates/index.html

    }

    // @GetMapping("/")
    // public String mainPage(Model model) {
    // List<String> pageNames = List.of("model", "increase", "fragments", "if",
    // "DTO", "querystring", "pathvariable");
    // model.addAttribute("pages", pageNames);
    // return "index"; // templates/index.html

    // }

    @GetMapping("/model")
    public String ex01Page(Model model) {
        model.addAttribute("hello", "만나서 반갑습니다. Spring Boot 시작합니다.");
        model.addAttribute("name", "sss");
        model.addAttribute("age", 20);
        return "ex01"; // templates/ex01.html

    }

    @GetMapping("/increase")
    public String ex02Page(Model model) {
        model.addAttribute("hello", "만나서 반갑습니다. Spring Boot 시작합니다.");
        model.addAttribute("name", "sss");
        model.addAttribute("age", 20);
        List<Integer> sampleNumbers = List.of(1, 2, 3, 4, 5, 6, 7);
        model.addAttribute("numbers", sampleNumbers);
        return "ex02"; // templates/ex02.html
    }

    @GetMapping("/fragments")
    public String ex03String(Model model) {
        return "ex03"; // templates/ex03.html
    }

    @GetMapping("/if")
    public String ex04String(Model model) {
        model.addAttribute("isAdmin", false);
        model.addAttribute("who", "김기윤");
        List<String> items = new ArrayList<>();
        items.add("사과");
        items.add("복숭아");
        items.add("바나나");
        items.add("수박");
        items.add("망고");
        items.add("포도");
        items.add("참외");
        model.addAttribute("items", items);
        return "ex04"; // templates/ex04.html
    }

    @GetMapping("/DTO")
    public String ex05(Model model) {

        MemberData member1 = new MemberData("홍길동", LocalDate.of(2001, 4, 3));
        MemberData member2 = new MemberData("슈퍼맨", LocalDate.of(1952, 10, 7));
        model.addAttribute("member1", member1);
        model.addAttribute("member2", member2);

        return "ex05";
    }

    @GetMapping("/BungBbang")
    public String ex06(Model model) {

        BungBbang 슈크림 = new BungBbang("슈크림", 1000, LocalDate.of(2025, 6, 4));
        BungBbang 팥 = new BungBbang("팥", 1500, LocalDate.of(2025, 6, 4));
        model.addAttribute("슈크림", 슈크림);
        model.addAttribute("팥", 팥);

        return "ex06";
    }

    @GetMapping("/querystring")
    public String ex07(@RequestParam(required = false) String inName, String inAge, String inGen, String want,
            String allow, Model model) {

        System.out.println("이름:" + inName);
        System.out.println("나이:" + inAge);
        System.out.println("성별:" + inGen);
        System.out.println("언어:" + want);
        System.out.println("동의:" + allow);

        List<String> content = List.of(
                "이름:" + inName,
                "나이:" + inAge,
                "성별:" + inGen,
                "언어:" + want,
                "동의:" + allow);

        boolean hasNull = inName == null || inName == "" || inAge == null || inAge == "" || inGen == null
                || want == null
                || allow == null;

        model.addAttribute("content", content);
        model.addAttribute("hasNull", hasNull); // 👉 템플릿에서 사용할 조건

        return "ex07";
    }

}
