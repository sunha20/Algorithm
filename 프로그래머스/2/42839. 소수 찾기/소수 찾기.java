import java.util.*;

class Solution {
    private int[] visited;
    private String[] numCard;
    private int N;
    private Set<Integer> set = new HashSet<>();
    public int solution(String numbers) {
        N = numbers.length();
        numCard = numbers.split("");
        visited = new int[N];   
        
        for (int i=0; i<N; i++){            
            bfs(i, 0);
        }
        
        int cnt = 0;
        for (int s: set) {
           cnt += confirmPrime(s); 
        }
        return cnt;
    }
    

    
    private void bfs(int idx, int result){
        int num = Integer.parseInt(numCard[idx]);
        if (visited[idx] == 1) return;

        visited[idx] = 1;
        int now = result*10+num;
        
        set.add(now);
        for (int i=0; i<N; i++) {
            bfs(i, now);
        }
        
        visited[idx] = 0;
    }
    
    private int confirmPrime(int num) {
        if (num == 0 || num == 1) { return 0; }
        for (int i=2; i<=Math.sqrt(num); i++) {
            if (num % i == 0) {
                return 0;
            }
        }
        return 1;
    }
}