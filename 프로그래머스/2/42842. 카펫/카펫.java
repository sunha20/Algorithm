import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        int h = 1; 
        int w = brown/2 - h;
        int generateY = 0;
        while (h <= w) {
            generateY = h * (w-2);
            if (generateY == yellow) break;
            h += 1;
            w -= 1;               
        }
        
        int[] answer = {w, h+2};
        return answer;
    }
}