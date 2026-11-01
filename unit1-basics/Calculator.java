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
