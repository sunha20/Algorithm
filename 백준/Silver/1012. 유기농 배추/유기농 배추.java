import java.io.*;
import java.util.*;

public class Main {
    static int[][] field;
    static int[][] visited;
    static final int[] X = {0,0,-1,1};
    static final int[] Y = {-1,1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int M, N, K;
        int bug;
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            // 밭 만들기
            st = new StringTokenizer(br.readLine(), " ");
            M = Integer.parseInt(st.nextToken());
            N = Integer.parseInt(st.nextToken());
            K = Integer.parseInt(st.nextToken());
            field = new int[M][N];
            visited = new int[M][N];

            // 밭 채우기
            for (int k = 0; k < K; k++) {
                st = new StringTokenizer(br.readLine(), " ");
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                field[x][y] = 1;
            }

            // 밭 탐색
            bug = 0;
            for (int n = 0; n < N; n++) {
                for (int m = 0; m < M; m++) {
                    if (field[m][n] == 1 && visited[m][n] == 0) {
                        //bfs(m, n);
                        dfs(m, n);
                        bug++;
                    }
                    visited[m][n] = 1;
                }
            }
            System.out.println(bug);
        }
        br.close();

    }

    public static void dfs(int x, int y) {
        visited[x][y] = 1;
        int endX = field.length - 1;
        int endY = field[0].length - 1;

        for (int i = 0; i < 4; i++) {
            int nx = x + X[i];
            int ny = y + Y[i];
            if (nx > endX || ny > endY || nx < 0 || ny < 0) continue;
            if (field[nx][ny] == 0 || visited[nx][ny] == 1) continue;
            visited[nx][ny] = 1;
            dfs(nx, ny);
        }
    }


    public static void bfs(int x, int y) {
        Queue<List<Integer>> que = new LinkedList<>();
        que.offer(new ArrayList(Arrays.asList(x, y)));
        int endX = field.length - 1;
        int endY = field[0].length - 1;

        while (!que.isEmpty()) {
            List<Integer> nowNode = que.poll();
            for (int i = 0; i < 4; i++) {
                int nx = nowNode.get(0) + X[i];
                int ny = nowNode.get(1) + Y[i];
                if (nx > endX || ny > endY || nx < 0 || ny < 0) continue;
                if (field[nx][ny] == 0 || visited[nx][ny] == 1) continue;
                que.offer(new ArrayList(Arrays.asList(nx, ny)));
                visited[nx][ny] = 1;
            }
        }

    }
}