package com.pknu.my01.controller;

import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

import com.pknu.my01.dto.ChatRequest;
import com.pknu.my01.service.OpenAiService;

@Controller
public class My02Controller {

    private final OpenAiService openAiService;

    public My02Controller(OpenAiService openAiService) {
        this.openAiService = openAiService;
    }

    @GetMapping("/final_chatbot")
    public String ex10Chat(Model model) {
        return "ex10a";
    }

    @PostMapping("/final_chatbot")
    @ResponseBody
    public Map<String, String> chat(@RequestBody ChatRequest request) {
        System.out.println(request.getMessage());
        String message = request.getMessage();
        String answer;
        if ("안녕".equals(message)) {
            answer = "안녕하세요.";
        } else if ("배고파".equals(message)) {
            // openai()
            answer = "저런 배가 많이 고프신가요?";
        } else {
            answer = openAiService.ask(message);
            // answer = "아직 업데이트 중이에요";
        }

        return Map.of("reply", answer);
    }

}
