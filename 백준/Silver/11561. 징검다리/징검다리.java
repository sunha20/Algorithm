import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i=0; i < T; i++) {
            long N = Long.parseLong(br.readLine());
            System.out.println(getNumOfJump(N));
        }
    }

    private static long getNumOfJump(long n){
        long hi = 1000000000;
        long lo = 1;
        long mid, now;
        
        while (lo + 1 < hi) {
            mid = (hi+lo)/2;
            now = mid*(mid+1) / 2;

            if (now == n) {
                lo = mid;
                break;
            }

            if (now < n) {
                lo = mid;
                continue;
            }

            if (now >= n) {
                hi = mid;
            }
        }
        return lo;
    }
}