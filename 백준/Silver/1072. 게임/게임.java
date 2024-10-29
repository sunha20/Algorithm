import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        long X = Integer.parseInt(temp[0]);
        long Y = Integer.parseInt(temp[1]);
        long Z = (Y * 100 / X);
        if (Z == 100) {
            System.out.println(-1);
            return;
        }

        long lo = 0;
        long hi = 1000000000;
        long mid, now;

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

    private static long getWinRate(long x, long y, long i) {
        return ((y+i) * 100/(x+i));
    }
}