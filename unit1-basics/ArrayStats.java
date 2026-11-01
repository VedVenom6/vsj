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
