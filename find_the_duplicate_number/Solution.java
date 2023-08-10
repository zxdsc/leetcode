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
