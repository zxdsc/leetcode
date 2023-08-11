// first i tried to do it with arithmetical sum
// but it founds out that input array can have more
// then one repeated element.


// one of the approaches is marking elements.
class Solution {
    public int findDuplicate(int[] nums) {
        for (int num : nums) {
            int idx = Math.abs(num);
            if (nums[idx] < 0) {
                return idx;
            } else {
                nums[idx] = -nums[idx];
            }
        }
        return -1;
    }
}

// one of the approache is fast and slow pointers
// we can do it in the same manner just run
// thorugh values as indexes
// the logic is next:
// if there is repeated element then 
// if we will treat it like index
// it will return us back in the array

class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0;
        int fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow;    
        }
}

// binary search
// we select middle from 1 to n range
// then count elements >= middle
// if counted elements > middle
// then we should check right part

class Solution {
    public int findDuplicate(int[] nums) {
        int len = nums.length;
        int left = 1;
        int right = len - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            int cnt = 0;
            for(int num: nums) {
                if (num <= mid) {
                    ++cnt;
                }
            }

            if (cnt <= mid) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
