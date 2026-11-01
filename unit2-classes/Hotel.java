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
