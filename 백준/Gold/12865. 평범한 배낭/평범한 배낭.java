import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static final int Weight = 0;
    static final int Value = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] goods = new int[N+1][2];
        goods[0] = new int[] {0,0};
        for(int g=1; g<N+1; g++) {
            st = new StringTokenizer(br.readLine());
            goods[g][Weight] = Integer.parseInt(st.nextToken());
            goods[g][Value] = Integer.parseInt(st.nextToken());
        }

        int[][] bag = new int[N+1][K+1];


        // Bottom-Up
        for (int n=1; n<N+1; n++) {
            for (int k=1; k<K+1; k++) {
                int addN;
                int skipN = bag[n-1][k];
                if (k >= goods[n][Weight]) addN = bag[n-1][k-goods[n][Weight]] + + goods[n][Value];
                else addN = 0;
                bag[n][k] = Math.max(addN, skipN);
            }
        }

        System.out.println(bag[N][K]);
    }
}