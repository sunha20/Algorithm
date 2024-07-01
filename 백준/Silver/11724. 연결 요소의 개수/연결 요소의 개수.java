import java.util.*;
import java.io.*;

public class Main {
    static int[][] gp;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] line = br.readLine().split(" ");
        int N = Integer.parseInt(line[0]);              // node 개수
        int M = Integer.parseInt(line[1]);              // 간선 개수

        gp = new int[N + 1][N + 1];
        visited = new int[N + 1];
        for (int m = 0; m < M; m++) {
            line = br.readLine().split(" ");
            int x = Integer.parseInt(line[0]);
            int y = Integer.parseInt(line[1]);
            gp[x][y] = 1;
            gp[y][x] = 1;
        }

        int cnt = 0;
        for (int n = 1; n <= N; n++) {
            if (visited[n] == 0) {
                bfs(n);
                cnt ++;
            }
        }
        System.out.println(cnt);
    }

    static void bfs(int N) {
        visited[N] = 1;
        for (int i = 1; i < gp.length; i++) {
            if (gp[N][i] == 1 && visited[i] == 0) bfs(i);
        }
    }
}