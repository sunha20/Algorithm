import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        int ir = 0;
        for (int i=people.length-1; i>=0; i--) {
            // 사용한 건 -1fh qkRnrl
            // 가장 많이 가져가는 걸 일단 목표로 해보자.
            int inBoat = people[i];
            while (inBoat <= limit) {
                int possible = limit - inBoat;
                
                if (people[ir] <= possible) {
                    inBoat += people[ir];
                    ir += 1;
                    continue;
                } 
                break;
            }
            answer += 1;
            System.out.println(inBoat);
            if (ir >= i) {
                break;
            }
        }
        return answer;
    }
}
