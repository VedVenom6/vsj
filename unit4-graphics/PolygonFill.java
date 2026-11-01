// Lab B3: Concave polygon filled using Scan-line fill, Flood fill, Seed (boundary) fill
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.*;

public class PolygonFill extends JPanel {
    static final int W = 600, H = 500;
    BufferedImage img = new BufferedImage(W, H, BufferedImage.TYPE_INT_RGB);
    int color = Color.WHITE.getRGB();

    void plot(int x, int y) {
        if (x >= 0 && x < W && y >= 0 && y < H) img.setRGB(x, y, color);
    }

    void bresLine(int x1, int y1, int x2, int y2) {
        int dx = Math.abs(x2 - x1), dy = Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1, sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy;
        while (true) {
            plot(x1, y1);
            if (x1 == x2 && y1 == y2) break;
            int e2 = 2 * err;
            if (e2 > -dy) { err -= dy; x1 += sx; }
            if (e2 <  dx) { err += dx; y1 += sy; }
        }
    }

    void polygon(int[] xs, int[] ys) {
        for (int i = 0; i < xs.length; i++)
            bresLine(xs[i], ys[i], xs[(i + 1) % xs.length], ys[(i + 1) % ys.length]);
    }

    // ---- Scan-line fill ----
    void scanFill(int[] xs, int[] ys) {
        int n = xs.length;
        int ymin = Arrays.stream(ys).min().getAsInt();
        int ymax = Arrays.stream(ys).max().getAsInt();
        for (int y = ymin; y <= ymax; y++) {
            ArrayList<Integer> xi = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                int x1 = xs[i], y1 = ys[i], x2 = xs[(i + 1) % n], y2 = ys[(i + 1) % n];
                if (y1 == y2) continue;                                  // skip horizontal edges
                if (y1 > y2) { int t = x1; x1 = x2; x2 = t; t = y1; y1 = y2; y2 = t; }
                if (y >= y1 && y < y2)                                   // half-open rule for vertices
                    xi.add(x1 + (y - y1) * (x2 - x1) / (y2 - y1));
            }
            Collections.sort(xi);
            for (int j = 0; j + 1 < xi.size(); j += 2)                   // fill between pairs
                for (int x = xi.get(j); x <= xi.get(j + 1); x++) plot(x, y);
        }
    }

    // ---- Flood fill: replace connected pixels of the OLD interior colour (explicit stack) ----
    void floodFill(int x, int y, int newC) {
        int oldC = img.getRGB(x, y);
        if (oldC == newC) return;
        ArrayDeque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{x, y});
        while (!st.isEmpty()) {
            int[] p = st.pop();
            int px = p[0], py = p[1];
            if (px < 0 || py < 0 || px >= W || py >= H) continue;
            if (img.getRGB(px, py) != oldC) continue;
            img.setRGB(px, py, newC);
            st.push(new int[]{px + 1, py}); st.push(new int[]{px - 1, py});   // 4-connected
            st.push(new int[]{px, py + 1}); st.push(new int[]{px, py - 1});
        }
    }

    // ---- Seed / Boundary fill: fill until the BOUNDARY colour ----
    void boundaryFill(int x, int y, int fillC, int boundC) {
        ArrayDeque<int[]> st = new ArrayDeque<>();
        st.push(new int[]{x, y});
        while (!st.isEmpty()) {
            int[] p = st.pop();
            int px = p[0], py = p[1];
            if (px < 0 || py < 0 || px >= W || py >= H) continue;
            int cur = img.getRGB(px, py);
            if (cur == boundC || cur == fillC) continue;
            img.setRGB(px, py, fillC);
            st.push(new int[]{px + 1, py}); st.push(new int[]{px - 1, py});
            st.push(new int[]{px, py + 1}); st.push(new int[]{px, py - 1});
        }
    }

    /* Textbook recursive version (may stack-overflow on large areas):
       void flood(int x, int y, int oldC, int newC) {
           if (getpixel(x, y) == oldC) {
               putpixel(x, y, newC);
               flood(x + 1, y, oldC, newC); flood(x - 1, y, oldC, newC);
               flood(x, y + 1, oldC, newC); flood(x, y - 1, oldC, newC);
           }
       }
    */

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(img, 0, 0, null);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PolygonFill c = new PolygonFill();

        // concave polygon: arrow-head pointing down (dent at (300,230))
        int[] xs = {150, 300, 450, 300};
        int[] ys = {150, 230, 150, 400};

        System.out.print("Fill 1.Scan-line 2.Flood 3.Seed/Boundary: ");
        int ch = sc.nextInt();

        c.color = Color.WHITE.getRGB();
        c.polygon(xs, ys);                                  // outline
        c.color = Color.RED.getRGB();
        int seedX = 300, seedY = 300;                       // a point truly inside the polygon

        switch (ch) {
            case 1:  c.scanFill(xs, ys); break;
            case 2:  c.floodFill(seedX, seedY, Color.BLUE.getRGB()); break;
            default: c.boundaryFill(seedX, seedY, Color.GREEN.getRGB(), Color.WHITE.getRGB());
        }

        JFrame f = new JFrame("Polygon Filling");
        f.add(c);
        f.setSize(W + 20, H + 40);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
