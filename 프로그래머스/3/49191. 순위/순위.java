class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] rank = new int[n][n];
        
        for (int[] r: results) {
            rank[r[0]-1][r[1]-1] = 1;
            rank[r[1]-1][r[0]-1] = -1;
        }
        
        for (int k=0; k<n; k++) {
            for (int i=0; i<n; i++) {
                for (int j=0; j<n; j++) {
                    if (rank[i][k]==-1 && rank[k][j]==-1) {
                        rank[i][j] = -1;
                        rank[j][i] = 1;
                    }
                }
            }
        }
        
        for (int i=0; i<n; i++) {
            int zero = 1;
            for (int j=0; j<n; j++) {
                if (rank[i][j] == 0) zero -= 1;
            }
            if (zero == 0) answer += 1;
        }
        
        return answer;
    }
}