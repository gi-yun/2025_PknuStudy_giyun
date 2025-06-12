package com.pknu.my01_1.dto;

import java.time.LocalDate;

public class BungBbang {
    private String flavor;
    private int price;
    private LocalDate madeDate;

    public BungBbang(String flavor, int price, LocalDate madeDate) {
        this.flavor = flavor;
        this.price = price;
        this.madeDate = madeDate;

    }

    public String getFlavor() {
        return flavor;
    }

    public void setFlavor(String flavor) {
        this.flavor = flavor;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public LocalDate getMadeDate() {
        return madeDate;
    }

    public void setMadeDate(LocalDate madeDate) {
        this.madeDate = madeDate;
    }

}
