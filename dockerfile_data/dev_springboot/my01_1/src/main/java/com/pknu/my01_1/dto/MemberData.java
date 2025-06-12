package com.pknu.my01_1.dto;

import java.time.LocalDate;

public class MemberData {
    private String name;
    private LocalDate birthData;

    public MemberData(String name, LocalDate birthData) {
        this.name = name;
        this.birthData = birthData;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LocalDate getBirthData() {
        return birthData;
    }

    public void setBirthData(LocalDate birthData) {
        this.birthData = birthData;
    }

}
