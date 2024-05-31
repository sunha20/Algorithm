class Solution {
    
    public int solution(int[] numbers, int target) {
        int idx = 0;
        int cnt = checkTarget(numbers, target, 0, 0);
        return cnt;
    }
    
    private int checkTarget(int [] numbers, int target, int idx, int num) {
        if (idx == numbers.length) {
            if (num == target) return 1;
            else return 0;
        }
        
        return checkTarget(numbers, target, idx+1, num+numbers[idx]) + checkTarget(numbers, target, idx+1, num-numbers[idx]);
    }
}