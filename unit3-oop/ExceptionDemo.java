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
