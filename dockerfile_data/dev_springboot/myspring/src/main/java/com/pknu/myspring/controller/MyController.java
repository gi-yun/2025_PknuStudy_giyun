package com.pknu.myspring.controller;

import com.pknu.myspring.service.LottoService;
// import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@Controller
public class MyController {

    private final LottoService lottoService;

    // @Autowired
    public MyController(LottoService lottoService) {
        this.lottoService = lottoService;
    }

    @GetMapping("/")
    public String mainPage() {
        return "index";
    }

    // @GetMapping("/")
    // public String mainPage() {
    // return "redirect:/index.html";
    // }

    @GetMapping("/lotto")
    public String redirectToLottoPage() {
        return "redirect:/lotto.html";
    }

    @GetMapping("/lotto/recommend")
    @ResponseBody
    public List<List<Integer>> getLottoRecommendations() {
        return lottoService.generateLottoSets(10);
    }

    @GetMapping("/lotto/frequency")
    @ResponseBody
    public Map<Integer, Integer> getLottoFrequencies() {
        return lottoService.loadNumberWeights(); // <== service에서 공개된 메서드
    }
}
