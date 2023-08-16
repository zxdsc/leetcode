class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; ++i) {
            map.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; ++i) {
            Integer id = map.get(target - nums[i]);
            if (id != null && id != i) {
                result[0] = i;
                result[1] = id;
            }
        }
        return result;
    }
}