package missing_number;

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int fullSum = 0;
        int sum = 0;
        for (int i = 1; i <= n; ++i) {
            fullSum += i;
            sum += nums[i - 1];
        }
        return fullSum - sum;
    }
}