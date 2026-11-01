// Lab B1: DDA line (two rectangles: dotted + thick) and Bresenham line (diamond: dashed + solid)
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;

public class Lines extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();

    void plot(int x, int y) {                                  // putpixel
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    // style: 0 = solid, 1 = dotted, 2 = dashed, 3 = thick
    void plotStyled(int x, int y, int i, int style) {
        if (style == 1 && i % 4 != 0) return;
        if (style == 2 && i % 12 >= 8) return;
        plot(x, y);
        if (style == 3) { plot(x + 1, y); plot(x, y + 1); plot(x + 1, y + 1); }
    }

    void ddaLine(int x1, int y1, int x2, int y2, int style) {
        int dx = x2 - x1, dy = y2 - y1;
        int steps = Math.max(Math.abs(dx), Math.abs(dy));
        if (steps == 0) { plot(x1, y1); return; }
        double xinc = (double) dx / steps, yinc = (double) dy / steps;
        double x = x1, y = y1;
        for (int i = 0; i <= steps; i++) {
            plotStyled((int) Math.round(x), (int) Math.round(y), i, style);
            x += xinc;
            y += yinc;
        }
    }

    // Bresenham for all slopes/directions (integer arithmetic only)
    void bresLine(int x1, int y1, int x2, int y2, int style) {
        int dx = Math.abs(x2 - x1), dy = Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1, sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy, i = 0;
        while (true) {
            plotStyled(x1, y1, i++, style);
            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) { err -= dy; x1 += sx; }
            if (e2 <  dx) { err += dx; y1 += sy; }
        }
    }

    void ddaRect(int x1, int y1, int x2, int y2, int style) {
        ddaLine(x1, y1, x2, y1, style); ddaLine(x2, y1, x2, y2, style);
        ddaLine(x2, y2, x1, y2, style); ddaLine(x1, y2, x1, y1, style);
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Lines c = new Lines();

        c.color = Color.CYAN.getRGB();
        c.ddaRect(100, 100, 500, 400, 1);      // outer rectangle - DDA dotted
        c.ddaRect(150, 150, 450, 350, 3);      // inner rectangle - DDA thick

        c.color = Color.YELLOW.getRGB();       // diamond through midpoints of outer rectangle
        c.bresLine(300, 100, 500, 250, 2);     // Bresenham dashed
        c.bresLine(500, 250, 300, 400, 2);
        c.bresLine(300, 400, 100, 250, 0);     // Bresenham solid
        c.bresLine(100, 250, 300, 100, 0);

        JFrame f = new JFrame("DDA & Bresenham Lines");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
