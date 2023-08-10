// recursion + memoization of steps
class Solution {
    public int climbStairs(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return helper(n, memo);
    }

    private int helper(int n, Map<Integer, Integer> memo) {
        if (n == 0 || n == 1) {
            return 1;
        }
        if (!memo.containsKey(n)) {
            memo.put(n, helper(n - 1, memo) + helper(n - 2, memo));
        }
        return memo.get(n);
    }
}

// itteration

class Solution {
    public int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        int prev = 1;
        int cur = 1;
        int res = 0;
        for (int i = 2; i <= n; ++i) {
            res = prev + cur;
            prev = cur;
            cur = res;
        }
        return res;
    }
}