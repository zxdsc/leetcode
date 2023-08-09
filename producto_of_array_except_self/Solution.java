class Solution {
    public int[] productExceptSelf(int[] nums) {
        // we can find all prefix and suffix products
        // and the current product will be prefix[i-1] * suffix[i + 1]

        int n = nums.length;
        int prefix[] = new int[n];
        int suffix[] = new int[n];
        prefix[0] = 1;
        suffix[n - 1] = 1;

        for (int i = 1; i < n; ++i) {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for (int i = n - 2; i >= 0; --i) {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        int ans[] = new int[n];
        for (int i = 0; i < n; ++i) {
            ans[i] = prefix[i] * suffix[i];
        }
        return ans;
    }
}

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // we catually can skip creation of helper arrays
        // and compute everytihing in place.
        int n = nums.length;
        int ans[] = new int[n];
        Arrays.fill(ans, 1);
        int current = 1;
        for (int i = 0; i < n; ++i) {
            ans[i] *= current;
            current *= nums[i];
        }
        current = 1;
        for (int i = n - 1; i >=0; --i) {
            ans[i] *= current;
            current *= nums[i];
        }

        return ans;
    }
}