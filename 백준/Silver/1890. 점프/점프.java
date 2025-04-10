import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] game;
    static long[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine()) + 1;
        game = new int[N][N];
        dp = new long[N][N];
        StringTokenizer st;
        for (int i = 1; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < N; j++) {
                game[i][j] = Integer.parseInt(st.nextToken());
                dp[i][j] = -1;
            }
        }

        System.out.println(recursive(1, 1));
    }

    private static long recursive(int x, int y) {
        if (x == N - 1 && y == N - 1) {
            return 1;
        }

        if (x >= N || y >= N || game[x][y] == 0) {
            return 0;
        }

        if (dp[x][y] == -1) {
            dp[x][y] = recursive(x + game[x][y], y) + recursive(x, y + game[x][y]);
        }
        return dp[x][y];
    }

}