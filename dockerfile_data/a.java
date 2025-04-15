class Parent {
    public void setName(String param) {
        System.out.print("A");
    }

    public void setAge(int param_i) {
        System.out.print("B");
    }
}

class Child extends Parent {
    @Override
    public void setName(String param) {
        System.out.print("C");
    }

    public void setHeight(int param_h) {
        System.out.print("D");
    }

    public static void main(String[] args) {
        Child c = new Child();
        c.setName("홍길동"); // C 출력
        c.setAge(40); // B 출력
        c.setHeight(170); // D 출력
    }
}
