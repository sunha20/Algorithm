import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] game = new int[N][N];
        long[][] dp = new long[N][N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                game[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dp[0][0] = 1;

        for (int x = 0; x < game.length; x++) {
            for (int y = 0; y < game.length; y++) {
                int jump = game[x][y];
                if (jump == 0) continue;
                if (x+jump < N) dp[x+jump][y] += dp[x][y];
                if (y+jump < N) dp[x][y+jump] += dp[x][y];
            }
        }
        System.out.println(dp[N-1][N-1]);
    }

}