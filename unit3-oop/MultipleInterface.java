// Lab A5: Multiple inheritance using interfaces + polymorphism through interface references
interface Printable {
    int MAX_PAGES = 100;                       // public static final by default
    void print();
}

interface Scannable {
    void scan();
}

class Machine {
    void powerOn() { System.out.println("Machine powered on"); }
}

// extends one class AND implements two interfaces
class Printer extends Machine implements Printable, Scannable {
    public void print() { System.out.println("Printing document (max " + MAX_PAGES + " pages)"); }
    public void scan()  { System.out.println("Scanning document"); }
}

class PhotoCopier implements Printable {
    public void print() { System.out.println("Photocopying"); }
}

public class MultipleInterface {
    public static void main(String[] args) {
        Printer p = new Printer();
        p.powerOn();
        p.print();
        p.scan();

        // polymorphism: one interface reference, different objects
        Printable[] devices = { new Printer(), new PhotoCopier() };
        for (Printable d : devices) d.print();

        Scannable s = p;
        s.scan();
        // s.print();  // ERROR: a Scannable reference only sees scan()
    }
}
