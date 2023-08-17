class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maximum = 0
        while l < r:
            water = 0;
            if height[l] < height[r]:
                water = height[l] * (r - l)
                l += 1
            elif height[l] >= height[r]:
                water = height[r] * (r - l)
                r -= 1
            maximum = max(maximum, water)
        return maximum