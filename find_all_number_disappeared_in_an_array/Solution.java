package find_all_number_disappeared_in_an_array;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> allNumbers = new HashSet<>();
        for (int i = 0; i < nums.length; ++i) {
            allNumbers.add(nums[i]);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= nums.length; ++i) {
            if (!allNumbers.contains(i)) {
                result.add(i);
            }
        }
        return result;
    }
}

// with constant mem
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int index = 0;
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] < 0) {
                index = nums[i] * - 1 - 1;
            } else {
                index = nums[i] - 1;
            }

            if (nums[index] > 0) {
                nums[index] = -nums[index];
            }
        }

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] > 0) {
                result.add(i + 1);
            }
        }

        return result;
    }
}
