// Labs B6, B7, B8: 2D transformations with 3x3 homogeneous matrices
// translate, scale, rotate, shear, reflect about X/Y axis, rotate about an arbitrary point,
// on an equilateral triangle or a rhombus. White = original, red = transformed.
import javax.swing.*;
import java.awt.*;
import java.util.Scanner;

public class Transform2D extends JPanel {
    double[][] orig, result;                 // each row = {x, y, 1}

    static double[][] translate(double tx, double ty) {
        return new double[][]{{1, 0, tx}, {0, 1, ty}, {0, 0, 1}};
    }
    static double[][] scale(double sx, double sy) {
        return new double[][]{{sx, 0, 0}, {0, sy, 0}, {0, 0, 1}};
    }
    static double[][] rotate(double deg) {               // anticlockwise
        double t = Math.toRadians(deg), c = Math.cos(t), s = Math.sin(t);
        return new double[][]{{c, -s, 0}, {s, c, 0}, {0, 0, 1}};
    }
    static double[][] shear(double shx, double shy) {    // x' = x + shx*y, y' = y + shy*x
        return new double[][]{{1, shx, 0}, {shy, 1, 0}, {0, 0, 1}};
    }
    static double[][] reflectX() { return new double[][]{{1, 0, 0}, {0, -1, 0}, {0, 0, 1}}; }
    static double[][] reflectY() { return new double[][]{{-1, 0, 0}, {0, 1, 0}, {0, 0, 1}}; }

    static double[][] multiply(double[][] a, double[][] b) {
        double[][] r = new double[3][3];
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                for (int k = 0; k < 3; k++)
                    r[i][j] += a[i][k] * b[k][j];
        return r;
    }

    static double[][] apply(double[][] m, double[][] pts) {     // P' = M . P
        double[][] out = new double[pts.length][3];
        for (int p = 0; p < pts.length; p++)
            for (int i = 0; i < 3; i++)
                for (int k = 0; k < 3; k++)
                    out[p][i] += m[i][k] * pts[p][k];
        return out;
    }

    // rotation about arbitrary point = T(xr,yr) . R(theta) . T(-xr,-yr)
    static double[][] rotateAbout(double deg, double xr, double yr) {
        return multiply(translate(xr, yr), multiply(rotate(deg), translate(-xr, -yr)));
    }

    // scaling about a fixed point = T(xf,yf) . S(sx,sy) . T(-xf,-yf)
    static double[][] scaleAbout(double sx, double sy, double xf, double yf) {
        return multiply(translate(xf, yf), multiply(scale(sx, sy), translate(-xf, -yf)));
    }

    int sx(double x) { return getWidth() / 2 + (int) Math.round(x); }   // origin at centre
    int sy(double y) { return getHeight() / 2 - (int) Math.round(y); }  // flip y (maths axes)

    void drawShape(Graphics g, double[][] p, Color col) {
        g.setColor(col);
        for (int i = 0; i < p.length; i++) {
            int j = (i + 1) % p.length;
            g.drawLine(sx(p[i][0]), sy(p[i][1]), sx(p[j][0]), sy(p[j][1]));
        }
    }

    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.GRAY);
        g.drawLine(0, getHeight() / 2, getWidth(), getHeight() / 2);
        g.drawLine(getWidth() / 2, 0, getWidth() / 2, getHeight());
        drawShape(g, orig, Color.WHITE);
        drawShape(g, result, Color.RED);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Transform2D t = new Transform2D();
        t.setBackground(Color.BLACK);

        System.out.print("Shape 1.Equilateral triangle 2.Rhombus: ");
        if (sc.nextInt() == 1)
            t.orig = new double[][]{{0, 0, 1}, {100, 0, 1}, {50, 86.6, 1}};
        else
            t.orig = new double[][]{{0, 0, 1}, {60, 40, 1}, {0, 80, 1}, {-60, 40, 1}};

        System.out.println("1.Translate 2.Scale 3.Rotate 4.Shear 5.Reflect about X axis");
        System.out.println("6.Reflect about Y axis 7.Rotate about arbitrary point 8.Scale about fixed point");
        int ch = sc.nextInt();
        double[][] m;
        switch (ch) {
            case 1:  System.out.print("tx ty: ");   m = translate(sc.nextDouble(), sc.nextDouble()); break;
            case 2:  System.out.print("sx sy: ");   m = scale(sc.nextDouble(), sc.nextDouble()); break;
            case 3:  System.out.print("angle: ");   m = rotate(sc.nextDouble()); break;
            case 4:  System.out.print("shx shy: "); m = shear(sc.nextDouble(), sc.nextDouble()); break;
            case 5:  m = reflectX(); break;
            case 6:  m = reflectY(); break;
            case 7:  System.out.print("angle xr yr: ");
                     m = rotateAbout(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            default: System.out.print("sx sy xf yf: ");
                     m = scaleAbout(sc.nextDouble(), sc.nextDouble(), sc.nextDouble(), sc.nextDouble());
        }
        t.result = apply(m, t.orig);

        for (int i = 0; i < t.orig.length; i++)
            System.out.printf("(%.1f, %.1f) -> (%.1f, %.1f)%n",
                t.orig[i][0], t.orig[i][1], t.result[i][0], t.result[i][1]);

        JFrame f = new JFrame("2D Transformations");
        f.add(t);
        f.setSize(700, 600);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
