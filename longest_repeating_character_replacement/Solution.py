class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            maxRepeated = -1
            for _, v in count.items():
                maxRepeated = max(maxRepeated, v)
            length = r - l + 1
            if (length - maxRepeated) <= k:
                res = max(res, length)
            else:
                count[s[l]] -= 1
                l += 1
        return res
