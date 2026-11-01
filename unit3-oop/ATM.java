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
