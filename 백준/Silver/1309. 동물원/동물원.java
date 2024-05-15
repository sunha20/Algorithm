import java.io.*;

public class Main {
    public void Solution1_dynamic() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int totalLion = Integer.parseInt(br.readLine());
        if(totalLion == 1) {
            System.out.println(3);
            return;
        } else if(totalLion == 2) {
            System.out.println(7);
            return;
        }

        int box = totalLion*2;
        int[][] dp = new int[box][3];
        final int MOD = 9901;
        dp[0] = new int[]{1, 0, 0};
        dp[1] = new int[]{1, 1, 1};
        dp[2] = new int[]{3, 2 ,2};

        for (int lion=2; lion<totalLion; lion++) {
            dp[lion+1][0] = (dp[lion][0] + dp[lion][1] + dp[lion][2])%MOD;
            dp[lion+1][1] = (dp[lion][0] + dp[lion][2])%MOD;
            dp[lion+1][2] = (dp[lion][0] + dp[lion][1])%MOD;

        }

        System.out.println((dp[totalLion][0]+dp[totalLion][1]+dp[totalLion][2])%MOD);
        br.close();
    }
    public static void main(String[] args) throws IOException {
        new Main().Solution1_dynamic();
    }
}
