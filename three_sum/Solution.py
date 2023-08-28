class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique = set(nums)
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i - 1] == n:
                continue
            
            l, r = i + 1, len(nums) - 1
            while (l < r):
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                if threeSum < 0:
                    l += 1
                if threeSum == 0:
                    result.append([n, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return result
                