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
