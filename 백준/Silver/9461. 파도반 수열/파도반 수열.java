import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        long[] dp = new long[101];
        dp[1] = 1;
        dp[2] = 1;
        dp[3] = 1;
        dp[4] = 2;

        int N;
        int cnt = 4;
        StringBuilder sb = new StringBuilder();

        // loop: test case
        for (int t=0; t<T; t++) {
            N = Integer.parseInt(br.readLine());
            if (cnt < N) {
                // loop: dp -> if dp가 덜 차있으면
                for (int i=cnt; i<=N; i++) {
                    dp[i] = dp[i-3] + dp[i-2];
                }
                cnt = N;
            }
            sb.append(dp[N]).append('\n');
        }
        System.out.println(sb);
    }
}