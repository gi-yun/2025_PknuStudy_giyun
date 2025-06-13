package com.giyun.test01.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SpController {

    private Map<String, Object> savedData = new HashMap<>();

    @GetMapping("/list")
    @ResponseBody
    public List<String> getList() {
        List<String> fruits = new ArrayList<>();
        fruits.add("사과");
        fruits.add("딸기");
        fruits.add("바나나");
        System.out.println("과일 리스트 반환함");
        return fruits;
    }

    @PostMapping("/data")
    @ResponseBody
    public Map<String, Object> receiveData(@RequestBody Map<String, Object> payload) {
        savedData = payload;
        Object name = payload.get("name");
        Object age = payload.get("age");
        Object memo = payload.get("memo");
        System.out.println("데이터 저장됨: " + savedData);
        System.out.println("이름: " + name + " / 나이: " + age + " / 메모: " + memo);
        Map<String, Object> result = new HashMap<>();
        result.put("이름", name);
        result.put("나이", age);
        result.put("메모", memo);
        return result;
    }

    @GetMapping("/api")
    public Map<String, Object> getSavedData() {
        Map<String, Object> result = new HashMap<>();
        result.put("data", savedData);
        System.out.println("저장된 데이터 반환: " + savedData);
        return result;
    }
}
