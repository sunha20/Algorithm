import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int N;

        for (int t=0; t<T; t++) {
            N = Integer.parseInt(br.readLine());
            int i = 4;
            while (dp[N] == 0) {
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
                i++;
            }
            System.out.println(dp[N]);
        }
    }
}