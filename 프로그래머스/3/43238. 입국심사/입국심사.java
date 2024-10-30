class Solution {
    public long solution(int n, int[] times) {
long lo = 0;
        long hi = (n/times.length) * 1000000000L;
        long mid, now;

        // lower bound
        while (lo < hi) {
            mid = (lo+hi)/2;
            now = 0;
            for (int i=0; i<times.length; i++) {
                now += mid/times[i];
            }

            if (now < n) {
                lo = mid+1;
                continue;
            }

            if (now >= n){
                hi = mid;
            }
        }
        return lo;
    }
}