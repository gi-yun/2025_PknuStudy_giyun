package com.pknu.my01.service;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class OpenAiService {
    @Value("${openai.api.key}")
    private String apikey;

    public String ask(String prompt) {
        HttpHeaders headers = new HttpHeaders();
        headers.setBearerAuth(apikey);
        headers.setContentType(MediaType.APPLICATION_JSON);

        List<Map<String, Object>> messages = List.of(
                Map.of("role", "system", "content", "너는 고객응대용으로 만들어 졌고, 존댓말을 사용하며 간결하게 대답해줘"),
                Map.of("role", "user", "content", prompt));
        Map<String, Object> body = Map.of(
                "model", "gpt-4.1-nano", // gpt 모델 선정
                "messages", messages, // 메세지 입력
                "temperature", 0.1, // "창의성" 또는 무작위 의 온도 0~2까지
                "max_tokens", 100, // 최대 토큰 사용량
                "presence_penalty", 0.6, // 새로운 주제 유도
                "frequency_penalty", 0.5 // 반복 억제
        );
        HttpEntity<Map<String, Object>> request = new HttpEntity<>(body, headers);
        RestTemplate restTemplate = new RestTemplate();
        try {
            ResponseEntity<Map> response = restTemplate.exchange("https://api.openai.com/v1/chat/completions",
                    HttpMethod.POST,
                    request,
                    Map.class);
            List<Map<String, Object>> choices = (List<Map<String, Object>>) response.getBody().get("choices");
            Map<String, Object> message = (Map<String, Object>) choices.get(0).get("message");
            return (String) message.get("content");
        } catch (Exception e) {
            return "오류:" + e.getMessage();
        }
    }

}
