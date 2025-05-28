package com.pknu.myspring.service;

import org.springframework.core.io.ClassPathResource;
import org.springframework.stereotype.Service;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class LottoService {

    private static final String FILE_PATH = "data/lotto_number_counts.csv";

    public List<List<Integer>> generateLottoSets(int count) {
        Map<Integer, Integer> numberCounts = loadNumberWeights();
        int maxCount = Collections.max(numberCounts.values());

        List<Integer> numbers = new ArrayList<>(numberCounts.keySet());
        List<Integer> weights = numbers.stream()
                .map(n -> maxCount - numberCounts.get(n) + 1)
                .collect(Collectors.toList());

        List<List<Integer>> result = new ArrayList<>();

        for (int i = 0; i < count; i++) {
            Set<Integer> selected = new HashSet<>();

            // ✅ 1. 가중치 기반 번호 4개 선택 (중복 제거됨)
            while (selected.size() < 4) {
                int picked = weightedRandom(numbers, weights);
                selected.add(picked);
            }

            // ✅ 2. 나머지 2개는 무작위 번호로 중복 없이 채움
            Random randGen = new Random();
            while (selected.size() < 6) {
                int rand = randGen.nextInt(45) + 1;
                selected.add(rand);
            }

            List<Integer> full = new ArrayList<>(selected);
            Collections.sort(full);
            result.add(full);
        }

        return result;
    }

    private int weightedRandom(List<Integer> nums, List<Integer> weights) {
        int total = weights.stream().mapToInt(i -> i).sum();
        int r = new Random().nextInt(total);
        int acc = 0;
        for (int i = 0; i < nums.size(); i++) {
            acc += weights.get(i);
            if (r < acc)
                return nums.get(i);
        }
        return nums.get(nums.size() - 1); // fallback
    }

    public Map<Integer, Integer> loadNumberWeights() {
        Map<Integer, Integer> map = new HashMap<>();
        try {
            ClassPathResource resource = new ClassPathResource(FILE_PATH);
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(resource.getInputStream(), StandardCharsets.UTF_8))) {
                reader.readLine(); // skip header
                String line;
                while ((line = reader.readLine()) != null) {
                    String[] parts = line.split(",");
                    map.put(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return map;
    }
}
