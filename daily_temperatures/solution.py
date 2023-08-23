class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            curTemp = temperatures[i]
            while stack and stack[-1][0] < curTemp:
                stackT, stackIdx = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append((curTemp, i))
        return result