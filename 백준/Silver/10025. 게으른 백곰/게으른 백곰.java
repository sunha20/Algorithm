import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());   // 양동이 개수
        int K = Integer.parseInt(st.nextToken());   
        int move = 2 * K + 1;                       // 움직일 수 있는 전체 거리.
        
        int[] pen = new int[1000001];
        int len = 0;
        int sum = 0;
        for (int n=0; n<N; n++) {
            st = new StringTokenizer(br.readLine());
            int ice = Integer.parseInt(st.nextToken());
            int idx = Integer.parseInt(st.nextToken());
            pen[idx] = ice;
            if (idx > len) len = idx;               // 유효한 배열 크기 구하기
            if (idx < move) sum += ice;             // 초기 부분합 구하기
        }
        len++;

        int p1 = 0;                         // pointer 1
        int p2 = move;                      // pointer 2
        int max = sum;                      // 부분합의 최댓값 구하기.
        for (int i=1; i<(len-(move)); i++) {
            sum -= pen[p1];
            sum += pen[p2];
            p1++; p2++;
            if (sum > max) max = sum;
        }

        System.out.println(max);
    }
}