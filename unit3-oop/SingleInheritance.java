// Lab A4: Single inheritance, super(), protected, method overriding (+ multilevel bonus)
class Vehicle {
    protected String brand;
    protected int speed;

    Vehicle(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
        System.out.println("Vehicle constructor");
    }

    void start() { System.out.println(brand + " starting"); }
    void info()  { System.out.println("Brand: " + brand + ", Speed: " + speed); }
}

class Car extends Vehicle {
    private int doors;

    Car(String brand, int speed, int doors) {
        super(brand, speed);                 // parent constructor runs first
        this.doors = doors;
        System.out.println("Car constructor");
    }

    @Override
    void info() {
        super.info();                        // reuse parent version
        System.out.println("Doors: " + doors);
    }

    void honk() { System.out.println("Beep!"); }
}

class SportsCar extends Car {                // multilevel: Vehicle -> Car -> SportsCar
    SportsCar(String brand) {
        super(brand, 300, 2);
        System.out.println("SportsCar constructor");
    }

    @Override
    void start() { System.out.println(brand + " roars to life!"); }
}

public class SingleInheritance {
    public static void main(String[] args) {
        Car c = new Car("Honda", 180, 4);
        c.start();      // inherited
        c.info();       // overridden
        c.honk();       // own method

        System.out.println("---- multilevel ----");
        SportsCar s = new SportsCar("Ferrari");
        s.start();
        s.info();
    }
}
