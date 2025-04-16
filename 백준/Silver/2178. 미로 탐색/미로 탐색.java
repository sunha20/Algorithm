/**
 * 최소 경로 문제 -> BFS
 * 몇칸? -> visited에 누적하면 되겠구나!
 */

import java.util.*;
import java.io.*;

public class Main {
    private static int N, M;
    private static int[][] miro, visited;
    private static final int[][] move = new int[][] {{-1,0},{1,0},{0,-1},{0,1}};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        miro = new int[N+1][M+1];
        visited = new int[N+1][M+1];

        for (int n=1; n<N+1; n++) {
            String[] temp = br.readLine().split("");
            for (int m=1; m<M+1; m++) {
                miro[n][m] = Integer.parseInt(temp[m-1]);
            }
        }

        System.out.println(bfs());
    }

    private static int bfs() {
        Queue<int[]> que = new LinkedList<>();

        que.offer(new int[] {1,1});
        visited[1][1] = 1;

        while (!que.isEmpty()) {
            int[] node = que.poll();
            int x = node[0];
            int y = node[1];

            // 범위 내의 상하좌우 node를 불러온 다음, 이동 가능 한 칸(1)인 경우에 만 que에 삽입
            for (int i=0; i<4; i++) {
                int newX = x+move[i][0];
                int newY = y+move[i][1];
                if (validNode(newX, newY)) {
                    que.offer(new int[] {newX, newY});
                    visited[newX][newY] = 1;
                    miro[newX][newY] = miro[x][y] + 1;
                }
            }
        }

        return miro[N][M];
    }

    private static boolean validNode(int x, int y) {
        if (x < 1 || x > N) return false;
        if (y < 1 || y > M) return false;
        if (visited[x][y] == 1) return false;
        if (miro[x][y] == 0) return false;

        return true;
    }

}