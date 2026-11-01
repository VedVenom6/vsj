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
