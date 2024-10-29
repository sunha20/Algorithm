import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        double X = Integer.parseInt(temp[0]);
        double Y = Integer.parseInt(temp[1]);
        int Z = (int) (Y * 100 / X);
        if (Z == 100) {
            System.out.println(-1);
            return;
        }

        int lo = 0;
        int hi = 1000000000;
        int mid = 0, now;

        while (lo<hi) {
            mid = (lo+hi)/2;
            now = getWinRate(X, Y, mid);

            if (now <= Z) {
                lo = mid + 1;
                continue;
            }

            if (now > Z) {
                hi = mid;
            }
        }

        if (getWinRate(X, Y, hi) == Z) System.out.println(-1);
        else System.out.println(hi);
    }

    private static int getWinRate(double x, double y, int i) {
        return (int) ((y+i) * 100/(x+i));
    }
}