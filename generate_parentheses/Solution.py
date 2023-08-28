class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def rec(open, closed):
            if open == closed == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                rec(open + 1, closed)
                stack.pop()
            if closed < open:
                stack.append(")")
                rec(open, closed + 1)
                stack.pop()
        
        rec(0, 0)
        return res
        