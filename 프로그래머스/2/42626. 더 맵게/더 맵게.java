/*
목표: 모든 음식의 스코빌 지수 > K;
방법: 스코빌 지수가 가장 낮은 두개의 음식으로 새 음식을 만들기;

- 최소 힙 이용(by 우선순위 큐)
*/

import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> hp = new PriorityQueue<>();
        for (int s: scoville) {
            hp.add(s);
        }
        
        int cnt = 0;
        Integer minA;
        Integer minB;
        
        while (true) {
            // 가장 스코빌 지수가 낮은 음식 2개
            minA = hp.poll();
            minB = hp.poll();
            
            // 조건 체크1 (문제 조건상 항상 minA != null 만족)
            if (minA >= K) {
                return cnt;
            }
            // 조건 체크2
            if (minB == null) {
                return -1;
            }

            // 새로운 음식 추가 및, 시도 횟수 늘리기.
            int newFood = minA + (minB * 2);
            hp.add(newFood);
            cnt += 1;
        }
    }
}