// Unit 3: abstract class, abstract method, dynamic binding (runtime polymorphism), final, toString
abstract class Shape {
    final String unit = "sq units";            // final variable = constant

    abstract double area();                    // no body

    void display() {                           // concrete method
        System.out.println(getClass().getSimpleName() + " area = " + String.format("%.2f", area()) + " " + unit);
    }
}

class Circle extends Shape {
    double r;
    Circle(double r) { this.r = r; }
    double area() { return Math.PI * r * r; }
    @Override public String toString() { return "Circle(r=" + r + ")"; }   // from Object class
}

class Rect extends Shape {
    double l, b;
    Rect(double l, double b) { this.l = l; this.b = b; }
    double area() { return l * b; }
}

final class Square extends Rect {              // final class: cannot be extended
    Square(double s) { super(s, s); }
}

public class ShapesAbstract {
    public static void main(String[] args) {
        Shape[] shapes = { new Circle(2), new Rect(3, 4), new Square(5) };
        for (Shape s : shapes) s.display();    // same call, different behaviour

        Shape s = new Circle(1);               // parent reference, child object
        System.out.println(s);                 // calls Circle's toString()
        // Shape x = new Shape();              // ERROR: abstract class cannot be instantiated
    }
}
