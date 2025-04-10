import java.io.*;

public class Main {

    static final int Mod = 1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N + 1][10];
        dp[0] = new int[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        dp[1] = new int[]{0, 1, 1, 1, 1, 1, 1, 1, 1, 1};

        for (int i = 2; i < dp.length; i++) {
            dp[i][0] = dp[i - 1][1];
            for (int j = 1; j < 9; j++) {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % Mod;
            }
            dp[i][9] = dp[i - 1][8];
        }

        int result = 0;
        for (int k = 0; k < 10; k++) {
            result += dp[N][k];
            result %= Mod;
        }

        System.out.println(result);
    }
}