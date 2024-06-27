import java.util.*;
import java.io.*;

public class Main {
    static int[][] gp;
    static int[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // # of node
        int M = Integer.parseInt(st.nextToken()); // # of line
        int V = Integer.parseInt(st.nextToken()); // start node

        // create graph
        gp = new int[N+1][N+1];
        visited = new int[N+1];

        // fill graph
        for (int m=0; m<M; m++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            gp[x][y] = 1;
            gp[y][x] = 1;
        }
        visited[V] = 1;
        System.out.println(dfs(V, 1));
        visited[V] = 2;
        System.out.println(bfs(V, 2));
        br.close();
    }

    public static String dfs(int now, int flag){
        String result = now + "";
        for (int i=0; i<gp.length; i++) {
            if (gp[now][i] == 1 && visited[i] != flag) {
                visited[i] = flag;
                 result += (" " + dfs(i, flag));
            }
        }
        return result;
    }

    public static String bfs(int start, int flag){
        Queue<Integer> que = new LinkedList<Integer>();
        que.offer(start);
        String result="";
        while (!que.isEmpty()){
            int now = que.poll();
            result += now + " ";
            for (int i=0; i<gp.length; i++){
                if (gp[now][i] == 1 && visited[i] != flag) {
                    visited[i] = flag;
                    que.offer(i);
                }
            }
        }
        return result;
    }

}
