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
            int possible = limit - inBoat;
            if (possible >= people[ir]) {
                ir += 1;
            }
            answer += 1;
            if (ir >= i) {
                break;
            }
        }
        return answer;
    }
}
