class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        i = 0
        while True:
            if numbers[i] + numbers[n] > target:
                n -= 1
            elif numbers[i] + numbers[n] < target:
                i += 1
            elif numbers[i] + numbers[n] == target:
                return [i + 1, n + 1]
        return []