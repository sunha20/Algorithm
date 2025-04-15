/**
 * (5 * 5) 칸 | 1-25 | 3줄 빙고
 * 계속 탐색으로 지워?
 * 아니면 dic을 만들어서 (number: [x, y]) 위치 확인
 * list [[가로1, 가로2, 가로3, 가로4, 가로 5], [세로 1,2,3,4,5], [대각 1, 대각2]]
 */

import java.io.*;
import java.util.*;


public class Main {

    private static int X = 0;
    private static int Y = 5;
    private static int C = 10;

    public static void main(String[] args) throws IOException {
        Map<Integer, List<Integer>> numbers = new HashMap<>();
        int[] bingo = new int[12];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 철수가 적은 수
        for (int x = 0; x < 5; x++) {
            st = new StringTokenizer(br.readLine());
            for (int y = 0; y < 5; y++) {
                int num = Integer.parseInt(st.nextToken());
                numbers.put(num, new ArrayList<>(Arrays.asList(x, y)));
            }
        }

        // 사회자가 부르는 수
        int cnt=0;
        int complete = 0;
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                cnt += 1;

                int num = Integer.parseInt(st.nextToken());
                List<Integer> pos = numbers.get(num);
                int x = pos.get(0);
                int y = pos.get(1);

                bingo[X+x] += 1;
                bingo[Y+y] += 1;
                if (bingo[X+x] == 5) complete += 1;
                if (bingo[Y+y] == 5) complete += 1;

                if (x == y) {
                    bingo[C] += 1;
                    if (bingo[C] == 5) complete += 1;
                }
                if (x + y == 4) {
                    bingo[C+1] += 1;
                    if (bingo[C+1] == 5) complete += 1;
                }

                if (complete >= 3) {
                    System.out.println(cnt);
                    return;
                }
            }
        }
    }
}