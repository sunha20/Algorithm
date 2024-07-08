import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());   // 양동이 개수
        int K = Integer.parseInt(st.nextToken());   // 움직일 수 있는 거리.
        int move = 2 * K + 1;
        int allIce = 0;
        int len = 0;
        int[] pen = new int[1000001];
        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            int ice = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());
            pen[idx] = ice;
            allIce += ice;
            if (idx > len) len = idx;
        }
        len++;

        if (len <= move) {
            System.out.println(allIce);
            return;
        }

        int p1 = 0;
        int p2 = move;
        int sum = 0;
        for (int i=p1; i<(p2); i++) {
            sum += pen[i];
        }

        int max = sum;
        for (int i=1; i<(len-(move)); i++) {
            sum -= pen[p1];
            sum += pen[p2];
            p1++; p2++;
            if (sum > max) max = sum;
        }

        System.out.println(max);
    }
}