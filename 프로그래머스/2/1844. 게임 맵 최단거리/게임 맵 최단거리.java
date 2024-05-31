import java.util.*;
class Solution {
    static int[][] offset = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    public int solution(int[][] maps) {
        int[][] visited = new int[maps.length][maps[0].length];
        visited[0][0] = 1;
        bfs(maps, visited);        
        int answer = visited[maps.length-1][maps[0].length-1];
        if (answer == 0) answer = -1;
        return answer;
    }
    private void bfs(int[][] maps, int[][] visited) {        
        Queue<int[]> que = new LinkedList<>();
        que.offer(new int[] {0,0});
        
        while (!que.isEmpty()) {
            int[] node = que.poll();
            int r = node[0];
            int c = node[1];  
        
            // 인접 node들 que에 삽입
            for (int[] o : offset) {
                int newR = r+o[0];
                int newC = c+o[1];

                // out of index
                if (newR < 0 || newC < 0 || newR >= maps.length || newC >= maps[0].length) continue;
                // invaild node
                if (maps[newR][newC] == 0 || visited[newR][newC] != 0) continue;

                que.offer(new int[] {newR, newC});
                
                // visit 처리
                visited[newR][newC] = visited[r][c] + 1;
            }
        }

    }
}