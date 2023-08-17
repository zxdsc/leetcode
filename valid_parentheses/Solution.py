# mine
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == '(' or c == '[' or c == '{'):
                stack.append(c)
            else:
                if len(stack) != 0:
                    poped = stack.pop()
                    if not ((poped == '(' and c == ')') or (poped == '[' and c == ']') or (poped == '{' and c == '}')):
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


# better
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
