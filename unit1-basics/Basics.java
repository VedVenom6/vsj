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
