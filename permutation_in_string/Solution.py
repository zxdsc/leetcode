class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = defaultdict(int)
        countS2 = defaultdict(int)
        for i in range(len(s1)):
            countS1[s1[i]] += 1
            countS2[s2[i]] += 1
        
        matches = 0
        for i in range(ord('a'), ord('z') + 1):

            if countS1[chr(i)] == countS2[chr(i)]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            right = s2[r]
            countS2[right] += 1
            if countS2[right] == countS1[right]:
                matches += 1
            elif countS2[right] == countS1[right] + 1:
                matches -= 1

            left = s2[l]
            countS2[left] -= 1
            if countS2[left] == countS1[left]:
                matches += 1
            elif countS2[left] == countS1[left] - 1:
                matches -= 1

            l += 1

        return matches == 26