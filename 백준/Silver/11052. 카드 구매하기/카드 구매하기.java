import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] pack = new int[N + 1];
        for (int n = 1; n < N + 1; n++) {
            pack[n] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[N + 1];
        dp[0] = 0;
        dp[1] = pack[1];
        for (int i = 1; i < N + 1; i++) {
            dp[i] = pack[i];
            for (int j = 1; j < i + 1; j++) {
                dp[i] = Math.max(dp[i - j] + dp[j], dp[i]);
            }
        }

        System.out.println(dp[N]);
    }
}