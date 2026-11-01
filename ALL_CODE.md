# All OOPCG Java code in one file

Ordered by **syllabus lab number** (SPPU 2024 pattern, PCC-205-COM).
To use one: copy the code block into a file named exactly like the class (e.g. `ATM.java`), then `javac ATM.java` and `java ATM`.

## Index

**Group A – Java OOP**

- A1 – [Calculator](#calculator) – Calculator with user input, conditions, loops and error handling
- A2 – [Order](#order) – E-commerce order: overloaded constructors, user input, discount, invoice
- A3 – [Hotel](#hotel) – Hotel room booking with a 2D array: view, book, exit
- A4 – [SingleInheritance](#singleinheritance) – Single inheritance: subclass extends superclass and calls its methods
- A5 – [MultipleInterface](#multipleinterface) – Multiple inheritance using interfaces, polymorphism
- A6 – [ATM](#atm) – ATM: try/catch/finally, ArithmeticException (insufficient funds), IllegalArgumentException (invalid input)
- A7 – [Chat](#chat) – Multithreaded chat: isAlive(), join(), priorities, suspend/resume/stop

**Group B – Computer Graphics**

- B1 – [Lines](#lines) – DDA rectangles (dotted, thick) + Bresenham diamond (dashed, solid)
- B2 – [Circles](#circles) – Menu: DDA / Bresenham / Midpoint circle, solid / dotted / dashed
- B3 – [PolygonFill](#polygonfill) – Concave polygon: scan-line, flood and seed fill
- B4 – [SutherlandHodgeman](#sutherlandhodgeman) – Sutherland-Hodgeman polygon clipping, vertices entered interactively
- B5 – [CohenSutherland](#cohensutherland) – Cohen-Sutherland line clipping
- B6, B7, B8 – [Transform2D](#transform2d) – 2D translate / rotate / scale / shear / reflect; triangle & rhombus; rotation about arbitrary point

**Extra practice (not on the lab list)**

- [Basics](#basics) – Data types, operators, if/else, switch, loops
- [ArrayStats](#arraystats) – Array input: sum, largest, even count
- [StudentDemo](#studentdemo) – Class, constructors, this, static, overloading, array of objects
- [ArgsAndIO](#argsandio) – Varargs, command-line args, BufferedReader
- [ShapesAbstract](#shapesabstract) – Abstract class, dynamic binding
- [ExceptionDemo](#exceptiondemo) – Built-in exceptions, nested try, throws, custom exception
- [ThreadBasics](#threadbasics) – Threads, Runnable, synchronized
- [Transform3D](#transform3d) – 3D translate / scale / rotate (cube)

---

# Group A – Java OOP

## Calculator
**Lab A1: Calculator with user input, conditions, loops and error handling**  
File: `unit1-basics/Calculator.java` · Run: `javac Calculator.java` → `java Calculator`

```java
// Lab A1: Menu-driven calculator (Unit 1: Scanner input, switch, do-while, break/continue)
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n1.Add 2.Sub 3.Mul 4.Div 5.Mod 0.Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            if (choice == 0) break;
            if (choice < 0 || choice > 5) {
                System.out.println("Invalid choice");
                continue;
            }

            System.out.print("Enter two numbers: ");
            double a = sc.nextDouble();
            double b = sc.nextDouble();

            switch (choice) {
                case 1: System.out.println("Result = " + (a + b)); break;
                case 2: System.out.println("Result = " + (a - b)); break;
                case 3: System.out.println("Result = " + (a * b)); break;
                case 4:
                    if (b == 0) System.out.println("Error: divide by zero");
                    else System.out.println("Result = " + (a / b));
                    break;
                case 5:
                    if (b == 0) System.out.println("Error: divide by zero");
                    else System.out.println("Result = " + (a % b));
                    break;
            }
        } while (true);

        System.out.println("Bye!");
        sc.close();
    }
}
```

## Order
**Lab A2: E-commerce order: overloaded constructors, user input, discount, invoice**  
File: `unit2-classes/Order.java` · Run: `javac Order.java` → `java Order`

```java
// Lab A2: E-commerce order processing with overloaded constructors, discount, invoice
import java.util.Scanner;

class Product {
    String name;
    double price;
    int qty;

    Product() { this("Sample", 0, 0); }
    Product(String name, double price) { this(name, price, 1); }   // qty defaults to 1
    Product(String name, double price, int qty) {
        this.name = name;
        this.price = price;
        this.qty = qty;
    }

    double total() { return price * qty; }
}

public class Order {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Product[] cart = new Product[10];
        cart[0] = new Product("Pen", 20);           // 2-arg constructor
        cart[1] = new Product("Notebook", 60, 3);   // 3-arg constructor
        int n = 2;

        System.out.print("How many more products? ");
        int extra = sc.nextInt();
        for (int i = 0; i < extra && n < cart.length; i++) {
            System.out.print("Name Price Qty: ");
            cart[n++] = new Product(sc.next(), sc.nextDouble(), sc.nextInt());
        }

        double sum = 0;
        System.out.println("\n------- INVOICE -------");
        for (int i = 0; i < n; i++) {
            Product p = cart[i];
            System.out.printf("%-10s %3d x %8.2f = %9.2f%n", p.name, p.qty, p.price, p.total());
            sum += p.total();
        }

        double disc;
        if (sum > 5000) disc = 0.10;
        else if (sum > 2000) disc = 0.05;
        else disc = 0;

        System.out.println("-----------------------");
        System.out.printf("Subtotal : %.2f%n", sum);
        System.out.printf("Discount : %.2f (%.0f%%)%n", sum * disc, disc * 100);
        System.out.printf("Total    : %.2f%n", sum - sum * disc);
        sc.close();
    }
}
```

## Hotel
**Lab A3: Hotel room booking with a 2D array: view, book, exit**  
File: `unit2-classes/Hotel.java` · Run: `javac Hotel.java` → `java Hotel`

```java
// Lab A3: Hotel room booking using a 2D array (floors x rooms)
import java.util.Scanner;

public class Hotel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] rooms = new int[3][4];      // 0 = free, 1 = booked
        int ch;

        do {
            System.out.println("\n1.View 2.Book 3.Cancel 0.Exit");
            ch = sc.nextInt();
            switch (ch) {
                case 1:
                    for (int f = 0; f < rooms.length; f++) {
                        System.out.print("Floor " + (f + 1) + ": ");
                        for (int r = 0; r < rooms[f].length; r++)
                            System.out.print(rooms[f][r] == 0 ? "[ ] " : "[X] ");
                        System.out.println();
                    }
                    break;
                case 2:
                case 3: {
                    System.out.print("Floor (1-3) and Room (1-4): ");
                    int f = sc.nextInt() - 1, r = sc.nextInt() - 1;
                    if (f < 0 || f >= rooms.length || r < 0 || r >= rooms[0].length)
                        System.out.println("Invalid room");
                    else if (ch == 2 && rooms[f][r] == 1)
                        System.out.println("Already booked");
                    else if (ch == 3 && rooms[f][r] == 0)
                        System.out.println("Room is not booked");
                    else {
                        rooms[f][r] = (ch == 2) ? 1 : 0;
                        System.out.println(ch == 2 ? "Booked!" : "Cancelled!");
                    }
                    break;
                }
                case 0:
                    System.out.println("Thank you!");
                    break;
                default:
                    System.out.println("Invalid choice");
            }
        } while (ch != 0);
        sc.close();
    }
}
```

## SingleInheritance
**Lab A4: Single inheritance: subclass extends superclass and calls its methods**  
File: `unit3-oop/SingleInheritance.java` · Run: `javac SingleInheritance.java` → `java SingleInheritance`

```java
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
```

## MultipleInterface
**Lab A5: Multiple inheritance using interfaces, polymorphism**  
File: `unit3-oop/MultipleInterface.java` · Run: `javac MultipleInterface.java` → `java MultipleInterface`

```java
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
```

## ATM
**Lab A6: ATM: try/catch/finally, ArithmeticException (insufficient funds), IllegalArgumentException (invalid input)**  
File: `unit3-oop/ATM.java` · Run: `javac ATM.java` → `java ATM`

```java
// Lab A6: ATM with exception handling (try, multiple catch, finally, throw)
// ArithmeticException for insufficient funds, IllegalArgumentException for invalid amount
import java.util.InputMismatchException;
import java.util.Scanner;

class Account {
    private double balance;

    Account(double balance) { this.balance = balance; }

    double getBalance() { return balance; }

    void deposit(double amt) {
        if (amt <= 0)
            throw new IllegalArgumentException("Deposit must be positive");
        balance += amt;
    }

    void withdraw(double amt) {
        if (amt <= 0)
            throw new IllegalArgumentException("Withdrawal must be positive");
        if (amt > balance)
            throw new ArithmeticException("Insufficient funds");
        balance -= amt;
    }
}

public class ATM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Account acc = new Account(5000);
        int ch = -1;

        while (ch != 0) {
            System.out.println("\n1.Balance 2.Deposit 3.Withdraw 0.Exit");
            try {
                ch = sc.nextInt();
                switch (ch) {
                    case 1:
                        System.out.println("Balance: " + acc.getBalance());
                        break;
                    case 2:
                        System.out.print("Amount: ");
                        acc.deposit(sc.nextDouble());
                        System.out.println("Deposited. Balance: " + acc.getBalance());
                        break;
                    case 3:
                        System.out.print("Amount: ");
                        acc.withdraw(sc.nextDouble());
                        System.out.println("Collect cash. Balance: " + acc.getBalance());
                        break;
                    case 0:
                        System.out.println("Goodbye");
                        break;
                    default:
                        System.out.println("Invalid choice");
                }
            } catch (ArithmeticException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("Error: " + e.getMessage());
            } catch (InputMismatchException e) {
                System.out.println("Error: enter numbers only");
                sc.next();                       // discard the bad token
            } finally {
                System.out.println("-- transaction complete --");
            }
        }
        sc.close();
    }
}
```

## Chat
**Lab A7: Multithreaded chat: isAlive(), join(), priorities, suspend/resume/stop**  
File: `unit3-oop/Chat.java` · Run: `javac Chat.java` → `java Chat`

```java
// Lab A7: Multithreaded chat - isAlive(), join(), priorities, suspend/resume/stop.
// suspend()/resume()/stop() are deprecated (and throw UnsupportedOperationException in
// recent Java), so pausing and stopping are done safely with volatile flags.
class User extends Thread {
    private String[] msgs;
    private volatile boolean paused = false;
    private volatile boolean stopped = false;

    User(String name, String[] msgs) {
        super(name);
        this.msgs = msgs;
    }

    void pauseUser()  { paused = true; }
    void resumeUser() { paused = false; }
    void stopUser()   { stopped = true; }

    public void run() {
        for (String m : msgs) {
            if (stopped) break;
            while (paused && !stopped) {                 // "suspended"
                try { Thread.sleep(100); } catch (InterruptedException e) { }
            }
            if (stopped) break;
            System.out.println(getName() + " [P" + getPriority() + "]: " + m);
            try { Thread.sleep(500); } catch (InterruptedException e) { }
        }
        System.out.println(getName() + " left the chat");
    }
}

public class Chat {
    public static void main(String[] args) throws InterruptedException {
        User a = new User("Ved",   new String[]{"Hi", "How are you?", "What's up?", "Bye"});
        User b = new User("Amit",  new String[]{"Hello", "Good", "Studying", "See ya"});
        User c = new User("Admin", new String[]{"URGENT: server restart", "Done"});

        c.setPriority(Thread.MAX_PRIORITY);    // 10 - high-priority messages
        a.setPriority(Thread.NORM_PRIORITY);   // 5
        b.setPriority(Thread.MIN_PRIORITY);    // 1

        System.out.println("Ved alive before start? " + a.isAlive());   // false
        a.start(); b.start(); c.start();
        System.out.println("Ved alive after start?  " + a.isAlive());   // true

        Thread.sleep(600);
        b.pauseUser();   System.out.println(">> Amit suspended");
        Thread.sleep(1000);
        b.resumeUser();  System.out.println(">> Amit resumed");
        a.stopUser();    System.out.println(">> Ved stopped");

        a.join(); b.join(); c.join();          // main waits for all threads
        System.out.println("Ved alive after join?   " + a.isAlive());   // false
        System.out.println("Chat ended");
    }
}
```

---

# Group B – Computer Graphics

## Lines
**Lab B1: DDA rectangles (dotted, thick) + Bresenham diamond (dashed, solid)**  
File: `unit4-graphics/Lines.java` · Run: `javac Lines.java` → `java Lines`

```java
// Lab B1: DDA line (two rectangles: dotted + thick) and Bresenham line (diamond: dashed + solid)
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class Lines extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();

    void plot(int x, int y) {                                  // putpixel
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    // style: 0 = solid, 1 = dotted, 2 = dashed, 3 = thick
    void plotStyled(int x, int y, int i, int style) {
        if (style == 1 && i % 4 != 0) return;
        if (style == 2 && i % 12 >= 8) return;
        plot(x, y);
        if (style == 3) { plot(x + 1, y); plot(x, y + 1); plot(x + 1, y + 1); }
    }

    void ddaLine(int x1, int y1, int x2, int y2, int style) {
        int dx = x2 - x1, dy = y2 - y1;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));
        if (steps == 0) { plot(x1, y1); return; }
        double xinc = (double) dx / steps, yinc = (double) dy / steps;
        double x = x1, y = y1;
        for (int i = 0; i <= steps; i++) {
            plotStyled((int) Math.round(x), (int) Math.round(y), i, style);
            x += xinc;
            y += yinc;
        }
    }

    // Bresenham for all slopes/directions (integer arithmetic only)
    void bresLine(int x1, int y1, int x2, int y2, int style) {
        int dx = Math.abs(x2 - x1), dy = Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1, sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy, i = 0;
        while (true) {
            plotStyled(x1, y1, i++, style);
            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) { err -= dy; x1 += sx; }
            if (e2 <  dx) { err += dx; y1 += sy; }
        }
    }

    void ddaRect(int x1, int y1, int x2, int y2, int style) {
        ddaLine(x1, y1, x2, y1, style); ddaLine(x2, y1, x2, y2, style);
        ddaLine(x2, y2, x1, y2, style); ddaLine(x1, y2, x1, y1, style);
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Lines c = new Lines();

        c.color = Color.CYAN.getRGB();
        c.ddaRect(100, 100, 500, 400, 1);      // outer rectangle - DDA dotted
        c.ddaRect(150, 150, 450, 350, 3);      // inner rectangle - DDA thick

        c.color = Color.YELLOW.getRGB();       // diamond through midpoints of outer rectangle
        c.bresLine(300, 100, 500, 250, 2);     // Bresenham dashed
        c.bresLine(500, 250, 300, 400, 2);
        c.bresLine(300, 400, 100, 250, 0);     // Bresenham solid
        c.bresLine(100, 250, 300, 100, 0);

        JFrame f = new JFrame("DDA & Bresenham Lines");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

## Circles
**Lab B2: Menu: DDA / Bresenham / Midpoint circle, solid / dotted / dashed**  
File: `unit4-graphics/Circles.java` · Run: `javac Circles.java` → `java Circles`

```java
// Lab B2: Menu-driven circle drawing - DDA, Bresenham, Midpoint - solid / dotted / dashed
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Scanner;

public class Circles extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();
    int k = 0;                                                  // pixel counter for styles

    void plot(int x, int y) {
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    // style: 0 = solid, 1 = dotted, 2 = dashed
    void plotStyled(int x, int y, int i, int style) {
        if (style == 1 && i % 4 != 0) return;
        if (style == 2 && i % 12 >= 8) return;
        plot(x, y);
    }

    void plot8(int xc, int yc, int x, int y, int style) {      // 8-way symmetry
        plotStyled(xc + x, yc + y, k, style); plotStyled(xc - x, yc + y, k, style);
        plotStyled(xc + x, yc - y, k, style); plotStyled(xc - x, yc - y, k, style);
        plotStyled(xc + y, yc + x, k, style); plotStyled(xc - y, yc + x, k, style);
        plotStyled(xc + y, yc - x, k, style); plotStyled(xc - y, yc - x, k, style);
        k++;
    }

    void bresCircle(int xc, int yc, int r, int style) {
        int x = 0, y = r, d = 3 - 2 * r;
        while (x <= y) {
            plot8(xc, yc, x, y, style);
            if (d < 0) d += 4 * x + 6;
            else { d += 4 * (x - y) + 10; y--; }
            x++;
        }
    }

    void midCircle(int xc, int yc, int r, int style) {
        int x = 0, y = r, p = 1 - r;
        while (x <= y) {
            plot8(xc, yc, x, y, style);
            x++;
            if (p < 0) p += 2 * x + 1;                  // midpoint inside -> keep y
            else { y--; p += 2 * x - 2 * y + 1; }       // midpoint outside -> y--
        }
    }

    void ddaCircle(int xc, int yc, int r, int style) {
        int n = 0;
        while ((1 << n) <= r) n++;                      // 2^(n-1) <= r < 2^n
        double eps = 1.0 / (1 << n);
        double x = 0, y = r;
        int iters = (int) (2 * Math.PI / eps) + 1;
        for (int i = 0; i < iters; i++) {
            plotStyled(xc + (int) Math.round(x), yc + (int) Math.round(y), i, style);
            double xn = x + eps * y;
            double yn = y - eps * xn;
            x = xn; y = yn;
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Circles c = new Circles();

        System.out.print("Algorithm 1.DDA 2.Bresenham 3.Midpoint: ");
        int alg = sc.nextInt();
        System.out.print("Style 0.Solid 1.Dotted 2.Dashed: ");
        int style = sc.nextInt();
        System.out.print("Centre x y and radius (e.g. 300 250 150): ");
        int xc = sc.nextInt(), yc = sc.nextInt(), r = sc.nextInt();

        c.color = Color.GREEN.getRGB();
        switch (alg) {
            case 1:  c.ddaCircle(xc, yc, r, style); break;
            case 2:  c.bresCircle(xc, yc, r, style); break;
            default: c.midCircle(xc, yc, r, style);
        }

        JFrame f = new JFrame("Circle Drawing");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

## PolygonFill
**Lab B3: Concave polygon: scan-line, flood and seed fill**  
File: `unit4-graphics/PolygonFill.java` · Run: `javac PolygonFill.java` → `java PolygonFill`

```java
// Lab B3: Concave polygon filled using Scan-line fill, Flood fill, Seed (boundary) fill
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.*;

public class PolygonFill extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();

    void plot(int x, int y) {
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    void bresLine(int x1, int y1, int x2, int y2) {
        int dx = Math.abs(x2 - x1), dy = Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1, sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy;
        while (true) {
            plot(x1, y1);
            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) { err -= dy; x1 += sx; }
            if (e2 <  dx) { err += dx; y1 += sy; }
        }
    }

    void polygon(int[] xs, int[] ys) {
        for (int i = 0; i < xs.length; i++)
            bresLine(xs[i], ys[i], xs[(i + 1) % xs.length], ys[(i + 1) % ys.length]);
    }

    // ---- Scan-line fill ----
    void scanFill(int[] xs, int[] ys) {
        int n = xs.length;
        int ymin = Arrays.stream(ys).min().getAsInt();
        int ymax = Arrays.stream(ys).max().getAsInt();
        for (int y = ymin; y <= ymax; y++) {
            ArrayList<Integer> xi = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int x1 = xs[i], y1 = ys[i], x2 = xs[(i + 1) % n], y2 = ys[(i + 1) % n];
                if (y1 == y2) continue;                                  // skip horizontal edges
                if (y1 > y2) { int t = x1; x1 = x2; x2 = t; t = y1; y1 = y2; y2 = t; }
                if (y >= y1 && y < y2)                                   // half-open rule for vertices
                    xi.add(x1 + (y - y1) * (x2 - x1) / (y2 - y1));
            }
            Collections.sort(xi);
            for (int j = 0; j + 1 < xi.size(); j += 2)                   // fill between pairs
                for (int x = xi.get(j); x <= xi.get(j + 1); x++) plot(x, y);
        }
    }

    // ---- Flood fill: replace connected pixels of the OLD interior colour (explicit stack) ----
    void floodFill(int x, int y, int newC) {
        int oldC = img.getRGB(x, y);
        if (oldC == newC) return;
        ArrayDeque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{x, y});
        while (!st.isEmpty()) {
            int[] p = st.pop();
            int px = p[0], py = p[1];
            if (px < 0 || py < 0 || px >= W || py >= H) continue;
            if (img.getRGB(px, py) != oldC) continue;
            img.setRGB(px, py, newC);
            st.push(new int[]{px + 1, py}); st.push(new int[]{px - 1, py});   // 4-connected
            st.push(new int[]{px, py + 1}); st.push(new int[]{px, py - 1});
        }
    }

    // ---- Seed / Boundary fill: fill until the BOUNDARY colour ----
    void boundaryFill(int x, int y, int fillC, int boundC) {
        ArrayDeque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{x, y});
        while (!st.isEmpty()) {
            int[] p = st.pop();
            int px = p[0], py = p[1];
            if (px < 0 || py < 0 || px >= W || py >= H) continue;
            int cur = img.getRGB(px, py);
            if (cur == boundC || cur == fillC) continue;
            img.setRGB(px, py, fillC);
            st.push(new int[]{px + 1, py}); st.push(new int[]{px - 1, py});
            st.push(new int[]{px, py + 1}); st.push(new int[]{px, py - 1});
        }
    }

    /* Textbook recursive version (may stack-overflow on large areas):
       void flood(int x, int y, int oldC, int newC) {
           if (getpixel(x, y) == oldC) {
               putpixel(x, y, newC);
               flood(x + 1, y, oldC, newC); flood(x - 1, y, oldC, newC);
               flood(x, y + 1, oldC, newC); flood(x, y - 1, oldC, newC);
           }
       }
    */

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PolygonFill c = new PolygonFill();

        // concave polygon: arrow-head pointing down (dent at (300,230))
        int[] xs = {150, 300, 450, 300};
        int[] ys = {150, 230, 150, 400};

        System.out.print("Fill 1.Scan-line 2.Flood 3.Seed/Boundary: ");
        int ch = sc.nextInt();

        c.color = Color.WHITE.getRGB();
        c.polygon(xs, ys);                                  // outline
        c.color = Color.RED.getRGB();
        int seedX = 300, seedY = 300;                       // a point truly inside the polygon

        switch (ch) {
            case 1:  c.scanFill(xs, ys); break;
            case 2:  c.floodFill(seedX, seedY, Color.BLUE.getRGB()); break;
            default: c.boundaryFill(seedX, seedY, Color.GREEN.getRGB(), Color.WHITE.getRGB());
        }

        JFrame f = new JFrame("Polygon Filling");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

## SutherlandHodgeman
**Lab B4: Sutherland-Hodgeman polygon clipping, vertices entered interactively**  
File: `unit4-graphics/SutherlandHodgeman.java` · Run: `javac SutherlandHodgeman.java` → `java SutherlandHodgeman`

```java
// Lab B4: Sutherland-Hodgeman polygon clipping (vertices entered interactively)
import javax.swing.*;
import java.awt.*;
import java.util.*;
import java.util.List;

public class SutherlandHodgeman extends JPanel {
    static double xmin = 150, ymin = 150, xmax = 450, ymax = 350;
    List<double[]> original, clipped;

    // edges: 0 = left, 1 = right, 2 = bottom, 3 = top
    static boolean inside(double[] p, int e) {
        switch (e) {
            case 0:  return p[0] >= xmin;
            case 1:  return p[0] <= xmax;
            case 2:  return p[1] >= ymin;
            default: return p[1] <= ymax;
        }
    }

    static double[] intersect(double[] a, double[] b, int e) {
        double x, y;
        if (e == 0 || e == 1) {
            x = (e == 0) ? xmin : xmax;
            y = a[1] + (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0]);
        } else {
            y = (e == 2) ? ymin : ymax;
            x = a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]);
        }
        return new double[]{x, y};
    }

    static List<double[]> clipPolygon(List<double[]> poly) {
        for (int e = 0; e < 4; e++) {                          // one window edge at a time
            List<double[]> out = new ArrayList<>();
            int n = poly.size();
            for (int i = 0; i < n; i++) {
                double[] v1 = poly.get(i), v2 = poly.get((i + 1) % n);
                boolean in1 = inside(v1, e), in2 = inside(v2, e);
                if (in1 && in2)  out.add(v2);                                 // in -> in
                else if (in1)    out.add(intersect(v1, v2, e));               // in -> out
                else if (in2) { out.add(intersect(v1, v2, e)); out.add(v2); } // out -> in
                // out -> out : nothing
            }
            poly = out;                                         // output feeds next edge
            if (poly.isEmpty()) break;
        }
        return poly;
    }

    void drawPoly(Graphics g, List<double[]> p) {
        for (int i = 0; i < p.size(); i++) {
            double[] a = p.get(i), b = p.get((i + 1) % p.size());
            g.drawLine((int) Math.round(a[0]), (int) Math.round(a[1]),
                       (int) Math.round(b[0]), (int) Math.round(b[1]));
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.WHITE);
        g.drawRect((int) xmin, (int) ymin, (int) (xmax - xmin), (int) (ymax - ymin));
        g.setColor(Color.DARK_GRAY);
        drawPoly(g, original);                                  // before
        g.setColor(Color.ORANGE);
        drawPoly(g, clipped);                                   // after
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SutherlandHodgeman p = new SutherlandHodgeman();
        p.setBackground(Color.BLACK);

        System.out.print("Window xmin ymin xmax ymax (0 = default 150 150 450 350): ");
        double first = sc.nextDouble();
        if (first != 0) { xmin = first; ymin = sc.nextDouble(); xmax = sc.nextDouble(); ymax = sc.nextDouble(); }

        System.out.print("Number of polygon vertices (0 = sample triangle): ");
        int n = sc.nextInt();
        p.original = new ArrayList<>();
        if (n == 0) {
            p.original.add(new double[]{100, 300});
            p.original.add(new double[]{300, 80});
            p.original.add(new double[]{520, 300});
        } else {
            for (int i = 0; i < n; i++) {
                System.out.print("Vertex " + (i + 1) + " x y: ");
                p.original.add(new double[]{sc.nextDouble(), sc.nextDouble()});
            }
        }

        p.clipped = clipPolygon(p.original);
        System.out.println("Clipped polygon vertices:");
        for (double[] v : p.clipped) System.out.printf("(%.1f, %.1f)%n", v[0], v[1]);

        JFrame f = new JFrame("Sutherland-Hodgeman Polygon Clipping");
        f.add(p);
        f.setSize(620, 540);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

## CohenSutherland
**Lab B5: Cohen-Sutherland line clipping**  
File: `unit4-graphics/CohenSutherland.java` · Run: `javac CohenSutherland.java` → `java CohenSutherland`

```java
// Lab B5: Cohen-Sutherland line clipping (outcodes TBRL)
import javax.swing.*;
import java.awt.*;
import java.util.Scanner;

public class CohenSutherland extends JPanel {
    static final int INSIDE = 0, LEFT = 1, RIGHT = 2, BOTTOM = 4, TOP = 8;
    static int xmin = 150, ymin = 150, xmax = 450, ymax = 350;

    double[][] original;           // lines before clipping {x1,y1,x2,y2}
    double[][] clipped;            // after clipping (null = rejected)

    static int code(double x, double y) {
        int c = INSIDE;
        if (x < xmin) c |= LEFT;   else if (x > xmax) c |= RIGHT;
        if (y < ymin) c |= BOTTOM; else if (y > ymax) c |= TOP;
        return c;
    }

    // returns clipped line or null if rejected
    static double[] clip(double x1, double y1, double x2, double y2) {
        int c1 = code(x1, y1), c2 = code(x2, y2);
        while (true) {
            if ((c1 | c2) == 0) return new double[]{x1, y1, x2, y2};   // trivially accept
            if ((c1 & c2) != 0) return null;                           // trivially reject
            int out = (c1 != 0) ? c1 : c2;
            double x, y;
            if ((out & TOP) != 0)         { x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1); y = ymax; }
            else if ((out & BOTTOM) != 0) { x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1); y = ymin; }
            else if ((out & RIGHT) != 0)  { y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1); x = xmax; }
            else                          { y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1); x = xmin; }
            if (out == c1) { x1 = x; y1 = y; c1 = code(x1, y1); }
            else           { x2 = x; y2 = y; c2 = code(x2, y2); }
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.WHITE);
        g.drawRect(xmin, ymin, xmax - xmin, ymax - ymin);              // clipping window
        for (int i = 0; i < original.length; i++) {
            double[] o = original[i];
            g.setColor(Color.DARK_GRAY);                               // original (faint)
            g.drawLine((int) o[0], (int) o[1], (int) o[2], (int) o[3]);
            if (clipped[i] != null) {
                double[] cl = clipped[i];
                g.setColor(Color.GREEN);                               // visible part
                g.drawLine((int) Math.round(cl[0]), (int) Math.round(cl[1]),
                           (int) Math.round(cl[2]), (int) Math.round(cl[3]));
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        CohenSutherland p = new CohenSutherland();
        p.setBackground(Color.BLACK);

        System.out.println("Window: (" + xmin + "," + ymin + ") to (" + xmax + "," + ymax + ")");
        System.out.print("How many lines? (0 = use sample lines): ");
        int n = sc.nextInt();
        if (n == 0) {
            p.original = new double[][]{
                {50, 200, 550, 300},     // crosses window -> clipped both ends
                {200, 200, 400, 300},    // fully inside -> accepted
                {50, 50, 120, 100},      // fully outside (top-left) -> rejected
                {300, 50, 300, 450}      // vertical through window -> clipped
            };
        } else {
            p.original = new double[n][4];
            for (int i = 0; i < n; i++) {
                System.out.print("Line " + (i + 1) + " x1 y1 x2 y2: ");
                for (int j = 0; j < 4; j++) p.original[i][j] = sc.nextDouble();
            }
        }

        p.clipped = new double[p.original.length][];
        for (int i = 0; i < p.original.length; i++) {
            double[] o = p.original[i];
            p.clipped[i] = clip(o[0], o[1], o[2], o[3]);
            System.out.printf("Line %d: codes %4s %4s -> %s%n", i + 1,
                pad(code(o[0], o[1])), pad(code(o[2], o[3])),
                p.clipped[i] == null ? "REJECTED" :
                String.format("(%.1f,%.1f)-(%.1f,%.1f)", p.clipped[i][0], p.clipped[i][1], p.clipped[i][2], p.clipped[i][3]));
        }

        JFrame f = new JFrame("Cohen-Sutherland Line Clipping");
        f.add(p);
        f.setSize(620, 540);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }

    static String pad(int c) {                    // outcode as 4-bit string TBRL
        return String.format("%4s", Integer.toBinaryString(c)).replace(' ', '0');
    }
}
```

## Transform2D
**Lab B6, B7, B8: 2D translate / rotate / scale / shear / reflect; triangle & rhombus; rotation about arbitrary point**  
File: `unit5-transforms/Transform2D.java` · Run: `javac Transform2D.java` → `java Transform2D`

```java
// Labs B6, B7, B8: 2D transformations with 3x3 homogeneous matrices
// translate, scale, rotate, shear, reflect about X/Y axis, rotate about an arbitrary point,
// on an equilateral triangle or a rhombus. White = original, red = transformed.
import javax.swing.*;
import java.awt.*;
import java.util.Scanner;

public class Transform2D extends JPanel {
    double[][] orig, result;                 // each row = {x, y, 1}

    static double[][] translate(double tx, double ty) {
        return new double[][]{{1, 0, tx}, {0, 1, ty}, {0, 0, 1}};
    }
    static double[][] scale(double sx, double sy) {
        return new double[][]{{sx, 0, 0}, {0, sy, 0}, {0, 0, 1}};
    }
    static double[][] rotate(double deg) {               // anticlockwise
        double t = Math.toRadians(deg), c = Math.cos(t), s = Math.sin(t);
        return new double[][]{{c, -s, 0}, {s, c, 0}, {0, 0, 1}};
    }
    static double[][] shear(double shx, double shy) {    // x' = x + shx*y, y' = y + shy*x
        return new double[][]{{1, shx, 0}, {shy, 1, 0}, {0, 0, 1}};
    }
    static double[][] reflectX() { return new double[][]{{1, 0, 0}, {0, -1, 0}, {0, 0, 1}}; }
    static double[][] reflectY() { return new double[][]{{-1, 0, 0}, {0, 1, 0}, {0, 0, 1}}; }

    static double[][] multiply(double[][] a, double[][] b) {
        double[][] r = new double[3][3];
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < 3; k++)
                    r[i][j] += a[i][k] * b[k][j];
        return r;
    }

    static double[][] apply(double[][] m, double[][] pts) {     // P' = M . P
        double[][] out = new double[pts.length][3];
        for (int p = 0; p < pts.length; p++)
            for (int i = 0; i < 3; i++)
                for (int k = 0; k < 3; k++)
                    out[p][i] += m[i][k] * pts[p][k];
        return out;
    }

    // rotation about arbitrary point = T(xr,yr) . R(theta) . T(-xr,-yr)
    static double[][] rotateAbout(double deg, double xr, double yr) {
        return multiply(translate(xr, yr), multiply(rotate(deg), translate(-xr, -yr)));
    }

    // scaling about a fixed point = T(xf,yf) . S(sx,sy) . T(-xf,-yf)
    static double[][] scaleAbout(double sx, double sy, double xf, double yf) {
        return multiply(translate(xf, yf), multiply(scale(sx, sy), translate(-xf, -yf)));
    }

    int sx(double x) { return getWidth() / 2 + (int) Math.round(x); }   // origin at centre
    int sy(double y) { return getHeight() / 2 - (int) Math.round(y); }  // flip y (maths axes)

    void drawShape(Graphics g, double[][] p, Color col) {
        g.setColor(col);
        for (int i = 0; i < p.length; i++) {
            int j = (i + 1) % p.length;
            g.drawLine(sx(p[i][0]), sy(p[i][1]), sx(p[j][0]), sy(p[j][1]));
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.GRAY);
        g.drawLine(0, getHeight() / 2, getWidth(), getHeight() / 2);
        g.drawLine(getWidth() / 2, 0, getWidth() / 2, getHeight());
        drawShape(g, orig, Color.WHITE);
        drawShape(g, result, Color.RED);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Transform2D t = new Transform2D();
        t.setBackground(Color.BLACK);

        System.out.print("Shape 1.Equilateral triangle 2.Rhombus: ");
        if (sc.nextInt() == 1)
            t.orig = new double[][]{{0, 0, 1}, {100, 0, 1}, {50, 86.6, 1}};
        else
            t.orig = new double[][]{{0, 0, 1}, {60, 40, 1}, {0, 80, 1}, {-60, 40, 1}};

        System.out.println("1.Translate 2.Scale 3.Rotate 4.Shear 5.Reflect about X axis");
        System.out.println("6.Reflect about Y axis 7.Rotate about arbitrary point 8.Scale about fixed point");
        int ch = sc.nextInt();
        double[][] m;
        switch (ch) {
            case 1:  System.out.print("tx ty: ");   m = translate(sc.nextDouble(), sc.nextDouble()); break;
            case 2:  System.out.print("sx sy: ");   m = scale(sc.nextDouble(), sc.nextDouble()); break;
            case 3:  System.out.print("angle: ");   m = rotate(sc.nextDouble()); break;
            case 4:  System.out.print("shx shy: "); m = shear(sc.nextDouble(), sc.nextDouble()); break;
            case 5:  m = reflectX(); break;
            case 6:  m = reflectY(); break;
            case 7:  System.out.print("angle xr yr: ");
                     m = rotateAbout(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            default: System.out.print("sx sy xf yf: ");
                     m = scaleAbout(sc.nextDouble(), sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
        }
        t.result = apply(m, t.orig);

        for (int i = 0; i < t.orig.length; i++)
            System.out.printf("(%.1f, %.1f) -> (%.1f, %.1f)%n",
                t.orig[i][0], t.orig[i][1], t.result[i][0], t.result[i][1]);

        JFrame f = new JFrame("2D Transformations");
        f.add(t);
        f.setSize(700, 600);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
```

---

# Extra practice (not on the lab list)

## Basics
**Data types, operators, if/else, switch, loops**  
File: `unit1-basics/Basics.java` · Run: `javac Basics.java` → `java Basics`

```java
// Unit 1 syntax in one runnable file: data types, casting, operators, if/else, switch, all loops
import java.util.Scanner;

public class Basics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // ---- data types + casting ----
        int i = 10;
        double d = i;              // widening (automatic)
        double pi = 9.7;
        int cut = (int) pi;        // narrowing (manual) -> 9
        char c = 'A';
        boolean flag = true;
        System.out.println(i + " " + d + " " + cut + " " + c + " " + flag);

        // ---- operators ----
        int x = 10, y = 3;
        System.out.println("x/y = " + (x / y));                 // 3 (integer division)
        System.out.println("x%y = " + (x % y));                 // 1
        System.out.println("(double)x/y = " + ((double) x / y));
        System.out.println("max = " + ((x > y) ? x : y));       // ternary
        int a = 5;
        System.out.println(a++ + " " + a);                      // 5 6 (post-increment)
        System.out.println(++a + " " + a);                      // 7 7 (pre-increment)

        // ---- if / else-if ----
        System.out.print("Enter marks: ");
        int marks = sc.nextInt();
        if (marks >= 75) System.out.println("Distinction");
        else if (marks >= 40) System.out.println("Pass");
        else System.out.println("Fail");

        // ---- switch ----
        System.out.print("Enter day number (1-3): ");
        switch (sc.nextInt()) {
            case 1: System.out.println("Monday"); break;
            case 2: System.out.println("Tuesday"); break;
            case 3: System.out.println("Wednesday"); break;
            default: System.out.println("Invalid");
        }

        // ---- loops ----
        for (int k = 1; k <= 5; k++) System.out.print(k + " ");
        System.out.println();

        int n = 5;
        while (n > 0) { System.out.print(n + " "); n--; }
        System.out.println();

        int m = 10;
        do { System.out.println("do-while runs at least once, m = " + m); } while (m < 5);

        int[] arr = {4, 8, 15, 16, 23, 42};
        int sum = 0;
        for (int v : arr) sum += v;                              // for-each
        System.out.println("Sum = " + sum);

        // break and continue
        for (int k = 1; k <= 10; k++) {
            if (k % 2 == 0) continue;      // skip even
            if (k > 7) break;              // stop after 7
            System.out.print(k + " ");     // 1 3 5 7
        }
        System.out.println();
        sc.close();
    }
}
```

## ArrayStats
**Array input: sum, largest, even count**  
File: `unit1-basics/ArrayStats.java` · Run: `javac ArrayStats.java` → `java ArrayStats`

```java
// Practice: read n numbers, print sum, largest, and count of even numbers
import java.util.Scanner;

public class ArrayStats {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("How many numbers? ");
        int n = sc.nextInt();
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            System.out.print("Enter number " + (i + 1) + ": ");
            a[i] = sc.nextInt();
        }

        int sum = 0, max = a[0], even = 0;
        for (int v : a) {
            sum += v;
            if (v > max) max = v;
            if (v % 2 == 0) even++;
        }

        System.out.println("Sum = " + sum);
        System.out.println("Largest = " + max);
        System.out.println("Even count = " + even);
        sc.close();
    }
}
```

## StudentDemo
**Class, constructors, this, static, overloading, array of objects**  
File: `unit2-classes/StudentDemo.java` · Run: `javac StudentDemo.java` → `java StudentDemo`

```java
// Unit 2: class, fields, constructors (default/parameterized/copy), this, static,
// getters/setters, object as parameter, returning object, overloading, array of objects
class Student {
    private int roll;
    private String name;
    private double marks;
    static int count = 0;              // shared by all objects

    Student() {                        // default constructor
        this(0, "Unknown", 0);         // constructor chaining, must be first line
    }

    Student(int roll, String name, double marks) {   // parameterized
        this.roll = roll;
        this.name = name;
        this.marks = marks;
        count++;
    }

    Student(Student s) {               // copy constructor (written by hand in Java)
        this(s.roll, s.name, s.marks);
    }

    public String getName() { return name; }
    public double getMarks() { return marks; }
    public void setMarks(double m) {
        if (m >= 0 && m <= 100) marks = m;
        else System.out.println("Invalid marks");
    }

    Student topper(Student other) {    // object as parameter + returning object
        return (this.marks >= other.marks) ? this : other;
    }

    void show() { System.out.println(roll + " " + name + " " + marks); }       // overloading
    void show(String prefix) { System.out.println(prefix + ": " + name); }

    static int getCount() { return count; }
}

public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student(1, "Ved", 88);
        Student s2 = new Student(2, "Amit", 92);
        Student s3 = new Student(s1);
        Student s4 = new Student();

        s1.topper(s2).show("Topper");
        s3.setMarks(150);                      // Invalid marks
        s4.show();
        System.out.println("Objects: " + Student.getCount());

        Student[] list = { s1, s2, s3 };       // array of objects
        for (Student s : list) s.show();

        Student r = s1;                        // same object, two references
        r.setMarks(50);
        System.out.println("s1 marks now: " + s1.getMarks());   // 50.0
    }
}
```

## ArgsAndIO
**Varargs, command-line args, BufferedReader**  
File: `unit2-classes/ArgsAndIO.java` · Run: `javac ArgsAndIO.java` → `java ArgsAndIO`

```java
// Unit 2 extras: passing arrays, varargs, command-line args, BufferedReader, PrintWriter
// Run: java ArgsAndIO 10 20
import java.io.*;

public class ArgsAndIO {
    static void doubleAll(int[] a) {             // array passed by reference value -> original changes
        for (int i = 0; i < a.length; i++) a[i] *= 2;
    }

    static int sum(int... nums) {                // varargs: nums is an int[]
        int s = 0;
        for (int x : nums) s += x;
        return s;
    }

    public static void main(String[] args) throws IOException {
        // command-line arguments are always Strings
        if (args.length >= 2) {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            System.out.println("Args sum = " + (a + b));
        } else {
            System.out.println("Tip: run as  java ArgsAndIO 10 20");
        }

        int[] arr = {1, 2, 3};
        doubleAll(arr);
        System.out.println("After doubleAll: " + arr[0] + " " + arr[1] + " " + arr[2]);
        System.out.println("sum(1,2) = " + sum(1, 2) + ", sum(4,5,6) = " + sum(4, 5, 6));

        // BufferedReader: reads Strings only, so parse them
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter your name: ");
        String name = br.readLine();
        System.out.print("Enter your age: ");
        int age = Integer.parseInt(br.readLine().trim());

        // PrintWriter: character output stream, true = auto-flush
        PrintWriter pw = new PrintWriter(System.out, true);
        pw.println("Hello " + name + ", next year you will be " + (age + 1));
    }
}
```

## ShapesAbstract
**Abstract class, dynamic binding**  
File: `unit3-oop/ShapesAbstract.java` · Run: `javac ShapesAbstract.java` → `java ShapesAbstract`

```java
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
```

## ExceptionDemo
**Built-in exceptions, nested try, throws, custom exception**  
File: `unit3-oop/ExceptionDemo.java` · Run: `javac ExceptionDemo.java` → `java ExceptionDemo`

```java
// Unit 3: built-in exceptions, multiple catch, nested try, throw vs throws, custom exception
class InsufficientFundsException extends Exception {        // custom CHECKED exception
    InsufficientFundsException(String msg) { super(msg); }
}

public class ExceptionDemo {

    // throws: declares that this method may throw a checked exception
    static void withdraw(double bal, double amt) throws InsufficientFundsException {
        if (amt > bal) throw new InsufficientFundsException("Need " + (amt - bal) + " more");
        System.out.println("Withdrawn " + amt);
    }

    public static void main(String[] args) {
        // 1. multiple catch: specific first, general last
        try {
            int[] a = new int[3];
            a[5] = 10 / 2;
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic: " + e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Array index: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("General: " + e);
        } finally {
            System.out.println("finally always runs");
        }

        // 2. nested try: inner catch doesn't match, outer one handles it
        try {
            try {
                int x = 10 / 0;
            } catch (NullPointerException e) {
                System.out.println("Inner caught NPE");
            }
        } catch (ArithmeticException e) {
            System.out.println("Outer caught: " + e.getMessage());
        }

        // 3. NumberFormatException
        try {
            int n = Integer.parseInt("abc");
        } catch (NumberFormatException e) {
            System.out.println("Bad number format");
        }

        // 4. NullPointerException
        try {
            String s = null;
            System.out.println(s.length());
        } catch (NullPointerException e) {
            System.out.println("Null reference used");
        }

        // 5. custom checked exception: must be caught or declared
        try {
            withdraw(1000, 500);
            withdraw(1000, 1500);
        } catch (InsufficientFundsException e) {
            System.out.println("Custom: " + e.getMessage());
        }
    }
}
```

## ThreadBasics
**Threads, Runnable, synchronized**  
File: `unit3-oop/ThreadBasics.java` · Run: `javac ThreadBasics.java` → `java ThreadBasics`

```java
// Unit 3: main thread, Runnable, multiple threads, synchronized
class Counter {
    int count = 0;
    synchronized void inc() { count++; }        // only one thread at a time
}

class Task implements Runnable {                // Runnable = preferred way (class can still extend another)
    private Counter counter;
    Task(Counter counter) { this.counter = counter; }

    public void run() {
        for (int i = 0; i < 1000; i++) counter.inc();
        System.out.println(Thread.currentThread().getName() + " finished");
    }
}

public class ThreadBasics {
    public static void main(String[] args) throws InterruptedException {
        Thread main = Thread.currentThread();
        System.out.println("Main thread: " + main.getName() + ", priority " + main.getPriority());

        Counter c = new Counter();
        Thread t1 = new Thread(new Task(c), "Worker-1");
        Thread t2 = new Thread(new Task(c), "Worker-2");
        Thread t3 = new Thread(new Task(c), "Worker-3");

        t1.start(); t2.start(); t3.start();     // start() -> new thread -> run()
        t1.join(); t2.join(); t3.join();

        System.out.println("Final count = " + c.count + " (always 3000 thanks to synchronized)");
    }
}
```

## Transform3D
**3D translate / scale / rotate (cube)**  
File: `unit5-transforms/Transform3D.java` · Run: `javac Transform3D.java` → `java Transform3D`

```java
// Unit 5: 3D transformations with 4x4 homogeneous matrices (console output, no window)
// translate, scale, rotate about X / Y / Z axis, applied to the 8 corners of a unit cube
import java.util.Scanner;

public class Transform3D {
    static double[][] translate(double tx, double ty, double tz) {
        return new double[][]{{1,0,0,tx},{0,1,0,ty},{0,0,1,tz},{0,0,0,1}};
    }
    static double[][] scale(double sx, double sy, double sz) {
        return new double[][]{{sx,0,0,0},{0,sy,0,0},{0,0,sz,0},{0,0,0,1}};
    }
    static double[][] rotateX(double deg) {          // y' = y cos - z sin, z' = y sin + z cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{1,0,0,0},{0,c,-s,0},{0,s,c,0},{0,0,0,1}};
    }
    static double[][] rotateY(double deg) {          // z' = z cos - x sin, x' = z sin + x cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{c,0,s,0},{0,1,0,0},{-s,0,c,0},{0,0,0,1}};
    }
    static double[][] rotateZ(double deg) {          // x' = x cos - y sin, y' = x sin + y cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{c,-s,0,0},{s,c,0,0},{0,0,1,0},{0,0,0,1}};
    }

    static double[] apply(double[][] m, double[] p) {
        double[] r = new double[4];
        for (int i = 0; i < 4; i++)
            for (int k = 0; k < 4; k++)
                r[i] += m[i][k] * p[k];
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[][] cube = {
            {0,0,0,1},{1,0,0,1},{1,1,0,1},{0,1,0,1},
            {0,0,1,1},{1,0,1,1},{1,1,1,1},{0,1,1,1}
        };

        System.out.println("1.Translate 2.Scale 3.Rotate X 4.Rotate Y 5.Rotate Z");
        int ch = sc.nextInt();
        double[][] m;
        switch (ch) {
            case 1:  System.out.print("tx ty tz: "); m = translate(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            case 2:  System.out.print("sx sy sz: "); m = scale(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            case 3:  System.out.print("angle: ");    m = rotateX(sc.nextDouble()); break;
            case 4:  System.out.print("angle: ");    m = rotateY(sc.nextDouble()); break;
            default: System.out.print("angle: ");    m = rotateZ(sc.nextDouble());
        }

        for (double[] p : cube) {
            double[] q = apply(m, p);
            System.out.printf("(%.0f,%.0f,%.0f) -> (%.2f, %.2f, %.2f)%n", p[0], p[1], p[2], q[0], q[1], q[2]);
        }
    }
}
```
