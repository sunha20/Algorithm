import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());       // 나무 수  
        int M = Integer.parseInt(st.nextToken());       // 나무 길이  

        st = new StringTokenizer(br.readLine());
        int[] trees = new int[N];
        for (int n = 0; n < N; n++) {
            trees[n] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(trees);

        // 이진탐색 초기화
        int hi = trees[N-1]+1;
        int lo = 0;

        while (lo < hi) {
            int now = (hi+lo) / 2;
            long sum = 0;
            for (int n=N-1; n>=0; n--){
                if (trees[n] < now) break;
                sum += (trees[n] - now);
            }

            if (sum < M) {
                hi = now;
            } else {
                lo = now + 1;
            }
        }

        System.out.println(lo-1);
    }
}