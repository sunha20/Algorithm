import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int K = Integer.parseInt(st.nextToken());       // 가지고 있는 랜선 수
        int N = Integer.parseInt(st.nextToken());       // 필요한 랜선 수

        long[] lines = new long[N];
        long sum = 0;
        for (int k = 0; k < K; k++) {
            lines[k] = Integer.parseInt(br.readLine());
            sum += lines[k];
        }

        // 이진탐색 초기화
        long max = (sum/N)+1;
        long min = 0L;
        while (min < max) {
            long now = (max + min) / 2;      // now = 이번 loop에 사용한 mid값

            int cnt = 0;                    // now에 따라 생성되는 line개수
            for (long line: lines) {         // line 개수 세기
                cnt += line/now;
            }

            /*
            conut된 line(cnt)와 필요한 line(N) 수를 비교
            cnt < N -> 줄 개수가 더 많아져야함 = 줄 길이가 현재(now)보다 무조건 짧아야함.
            cnt >= N -> 줄 개수가 적어져야함. = 줄 길이가 현재(now)보다 무조건 길어야함 (+1).
            +) upper bound 방식이므로 N과 cnt가 같은 경우 min으로 설정해줌
               upper bound: 기준을 초과한 첫번째 값이 반환되도록 -> 던지는 값은 항상 low
             */
            if (cnt < N) {
                max = now;
            } else {
                min = now + 1;
            }

        }
        System.out.println(min-1);

    }
}