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
