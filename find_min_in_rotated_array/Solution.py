class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        mid = 0
        currentMin = float("inf")
        while l <= r:
            mid = l + ((r - l) // 2)
            currentMin = min(currentMin, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(currentMin, nums[l])
        