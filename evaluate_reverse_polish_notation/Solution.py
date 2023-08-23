class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
                if token == '+':
                    v2 = int(stack.pop())
                    v1 = int(stack.pop())
                    stack.append(v1 + v2)
                elif token == '-':
                    v2 = int(stack.pop())
                    v1 = int(stack.pop())
                    stack.append(v1 - v2)
                elif token == '*':
                    print(stack)
                    v2 = int(stack.pop())
                    v1 = int(stack.pop())
                    stack.append(v1 * v2)
                elif token == '/':
                    v2 = int(stack.pop())
                    v1 = int(stack.pop())
                    stack.append(int(v1 / v2))
                else:
                    stack.append(int(token))
        return stack.pop()

