import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] dp = new int[N + 1][10]; // [전체길이][A 선택]
        dp[1] = new int[]{1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

        int sum = 0;
        for (int i = 1; i < N + 1; i++) {
            dp[i][0] = 1;
            sum = dp[i][0];             // 전체 합을 구하기 위함.
            for (int j = 1; j < 10; j++) {
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 10007;
                sum = (sum + dp[i][j]) % 10007;                 // 모듈러 연산 필요(dp[i][j]가 모듈러 된 거라고 생각해서 넘겼는데, 둘을 더했을 때 값이 커질 것도 생각했어야함.)
            }
        }

        System.out.println(sum);
    }
}