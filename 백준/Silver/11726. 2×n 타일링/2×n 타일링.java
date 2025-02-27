import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] dp = new int[1001];
        dp[1] = 1;
        dp[2] = 2;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int cnt = 2;

        while (cnt < N) {
            cnt++;
            dp[cnt] = (dp[cnt-1] + dp[cnt-2]) % 10007;
        }

        System.out.println(dp[N]);
    }
}