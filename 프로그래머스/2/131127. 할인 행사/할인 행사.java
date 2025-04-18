/**
* 배열에서 삭제 연산하는 건 시간복잡도가 맣이 드니까... 사실 10개 이하라서 상관 없긴할 것같은데 그래도
* 1. Map 만들기
* 2. 슬라이딩 윈도우 처럼 discount 순회
*/

import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        Map<String, Integer> wantList = new HashMap<>();
        int cart = 0;
        int result = 0;
        
        for (int i=0; i< want.length; i++) {
            wantList.put(want[i], number[i]);
            cart += number[i];
        }
        
        // 끝부분 고려x
        for (int i=0; i<10; i++) {
            String item = discount[i];
            
            if (wantList.containsKey(item)) {
                wantList.put(item, wantList.get(item) - 1);
                if (wantList.get(item) >= 0) {
                    cart -= 1;
                }
            }
        }
        
        if (cart == 0) result += 1;
        
        for (int i = 10; i<discount.length; i++) {
            String item = discount[i];
            
            if (wantList.containsKey(item)) {
                wantList.put(item, wantList.get(item) - 1);
                if (wantList.get(item) >= 0) {
                    cart -= 1;
                }
            }
            
            
            item = discount[i-10];
            if (wantList.containsKey(item)) {
                wantList.put(item, wantList.get(item) + 1);
                if (wantList.get(item) > 0) {
                    cart += 1;
                }
            }
            
            if (cart == 0) result += 1;
        }

        return result;
    }
}