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
