// Lab B2: Menu-driven circle drawing - DDA, Bresenham, Midpoint - solid / dotted / dashed
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Scanner;

public class Circles extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();
    int k = 0;                                                  // pixel counter for styles

    void plot(int x, int y) {
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    // style: 0 = solid, 1 = dotted, 2 = dashed
    void plotStyled(int x, int y, int i, int style) {
        if (style == 1 && i % 4 != 0) return;
        if (style == 2 && i % 12 >= 8) return;
        plot(x, y);
    }

    void plot8(int xc, int yc, int x, int y, int style) {      // 8-way symmetry
        plotStyled(xc + x, yc + y, k, style); plotStyled(xc - x, yc + y, k, style);
        plotStyled(xc + x, yc - y, k, style); plotStyled(xc - x, yc - y, k, style);
        plotStyled(xc + y, yc + x, k, style); plotStyled(xc - y, yc + x, k, style);
        plotStyled(xc + y, yc - x, k, style); plotStyled(xc - y, yc - x, k, style);
        k++;
    }

    void bresCircle(int xc, int yc, int r, int style) {
        int x = 0, y = r, d = 3 - 2 * r;
        while (x <= y) {
            plot8(xc, yc, x, y, style);
            if (d < 0) d += 4 * x + 6;
            else { d += 4 * (x - y) + 10; y--; }
            x++;
        }
    }

    void midCircle(int xc, int yc, int r, int style) {
        int x = 0, y = r, p = 1 - r;
        while (x <= y) {
            plot8(xc, yc, x, y, style);
            x++;
            if (p < 0) p += 2 * x + 1;                  // midpoint inside -> keep y
            else { y--; p += 2 * x - 2 * y + 1; }       // midpoint outside -> y--
        }
    }

    void ddaCircle(int xc, int yc, int r, int style) {
        int n = 0;
        while ((1 << n) <= r) n++;                      // 2^(n-1) <= r < 2^n
        double eps = 1.0 / (1 << n);
        double x = 0, y = r;
        int iters = (int) (2 * Math.PI / eps) + 1;
        for (int i = 0; i < iters; i++) {
            plotStyled(xc + (int) Math.round(x), yc + (int) Math.round(y), i, style);
            double xn = x + eps * y;
            double yn = y - eps * xn;
            x = xn; y = yn;
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Circles c = new Circles();

        System.out.print("Algorithm 1.DDA 2.Bresenham 3.Midpoint: ");
        int alg = sc.nextInt();
        System.out.print("Style 0.Solid 1.Dotted 2.Dashed: ");
        int style = sc.nextInt();
        System.out.print("Centre x y and radius (e.g. 300 250 150): ");
        int xc = sc.nextInt(), yc = sc.nextInt(), r = sc.nextInt();

        c.color = Color.GREEN.getRGB();
        switch (alg) {
            case 1:  c.ddaCircle(xc, yc, r, style); break;
            case 2:  c.bresCircle(xc, yc, r, style); break;
            default: c.midCircle(xc, yc, r, style);
        }

        JFrame f = new JFrame("Circle Drawing");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
