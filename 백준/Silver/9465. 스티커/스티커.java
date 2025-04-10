import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

import static javax.swing.text.html.HTML.Attribute.N;

public class Main {

    static final int Mod = 1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine());

            int[][] stickers = new int[N + 1][2];
            stickers[0] = new int[]{0, 0};
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int x = 1; x < stickers.length; x++) {
                stickers[x] = new int[]{Integer.parseInt(st1.nextToken()), Integer.parseInt(st2.nextToken())};
            }

            int[][] dp = new int[N + 1][3];
            dp[0] = new int[]{0, 0, 0}; //위, 아래, 안뗌.
            for (int i = 1; i < stickers.length; i++) {
                dp[i][0] = Math.max(dp[i - 1][1], dp[i - 1][2]) + stickers[i][0];
                dp[i][1] = Math.max(dp[i - 1][0], dp[i - 1][2]) + stickers[i][1];
                dp[i][2] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            }
            System.out.println(Arrays.stream(dp[N]).max().getAsInt());
        }
    }

}