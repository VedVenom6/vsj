// Unit 5: 3D transformations with 4x4 homogeneous matrices (console output, no window)
// translate, scale, rotate about X / Y / Z axis, applied to the 8 corners of a unit cube
import java.util.Scanner;

public class Transform3D {
    static double[][] translate(double tx, double ty, double tz) {
        return new double[][]{{1,0,0,tx},{0,1,0,ty},{0,0,1,tz},{0,0,0,1}};
    }
    static double[][] scale(double sx, double sy, double sz) {
        return new double[][]{{sx,0,0,0},{0,sy,0,0},{0,0,sz,0},{0,0,0,1}};
    }
    static double[][] rotateX(double deg) {          // y' = y cos - z sin, z' = y sin + z cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{1,0,0,0},{0,c,-s,0},{0,s,c,0},{0,0,0,1}};
    }
    static double[][] rotateY(double deg) {          // z' = z cos - x sin, x' = z sin + x cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{c,0,s,0},{0,1,0,0},{-s,0,c,0},{0,0,0,1}};
    }
    static double[][] rotateZ(double deg) {          // x' = x cos - y sin, y' = x sin + y cos
        double c = Math.cos(Math.toRadians(deg)), s = Math.sin(Math.toRadians(deg));
        return new double[][]{{c,-s,0,0},{s,c,0,0},{0,0,1,0},{0,0,0,1}};
    }

    static double[] apply(double[][] m, double[] p) {
        double[] r = new double[4];
        for (int i = 0; i < 4; i++)
            for (int k = 0; k < 4; k++)
                r[i] += m[i][k] * p[k];
        return r;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[][] cube = {
            {0,0,0,1},{1,0,0,1},{1,1,0,1},{0,1,0,1},
            {0,0,1,1},{1,0,1,1},{1,1,1,1},{0,1,1,1}
        };

        System.out.println("1.Translate 2.Scale 3.Rotate X 4.Rotate Y 5.Rotate Z");
        int ch = sc.nextInt();
        double[][] m;
        switch (ch) {
            case 1:  System.out.print("tx ty tz: "); m = translate(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            case 2:  System.out.print("sx sy sz: "); m = scale(sc.nextDouble(), sc.nextDouble(), sc.nextDouble()); break;
            case 3:  System.out.print("angle: ");    m = rotateX(sc.nextDouble()); break;
            case 4:  System.out.print("angle: ");    m = rotateY(sc.nextDouble()); break;
            default: System.out.print("angle: ");    m = rotateZ(sc.nextDouble());
        }

        for (double[] p : cube) {
            double[] q = apply(m, p);
            System.out.printf("(%.0f,%.0f,%.0f) -> (%.2f, %.2f, %.2f)%n", p[0], p[1], p[2], q[0], q[1], q[2]);
        }
    }
}
