# with sorting - O(n log n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        result = []
        for key, val in sorted(map.items(), key=lambda item: item[1], reverse=True):
            if (k > 0):
                result.append(key)
            k -= 1
 
        return result

# Without sorting
# Idea: inverse map and create an array where
# index - count for value and value - list of 
# occured numbers [index] times

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        freq = [[] for i in range(len(nums) + 1)]
        for key, val in map.items():
            freq[val].append(key)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return result
