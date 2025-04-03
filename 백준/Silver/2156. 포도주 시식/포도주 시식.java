import java.io.*;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] wine = new int[N+1];
        int[] dp = new int[N+1];
        wine[0] = dp[0] = 0;
        wine[1] = dp[1] = Integer.parseInt(br.readLine());

        if (N==1) {
            System.out.println(dp[1]);
            return;
        }

        wine[2] = Integer.parseInt(br.readLine());
        dp[2] = wine[1] + wine[2];

        if (N==2) {
            System.out.println(dp[2]);
            return;
        }

        for (int n=3; n<N+1; n++) {
            wine[n] = Integer.parseInt(br.readLine());
            int nowX = dp[n-1];
            int prev1X = dp[n-2] + wine[n];
            int prev2X = dp[n-3] + wine[n] + wine[n-1];

            dp[n] = Math.max(nowX, Math.max(prev1X, prev2X));
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}