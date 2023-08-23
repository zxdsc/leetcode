class MinStack:

    def __init__(self):
        self.min = []
        self.struct = []

    def push(self, val: int) -> None:
        self.struct.append(val)
        if len(self.min) != 0:
            if self.min[-1] < val:
                self.min.append(self.min[-1])
            else:
                self.min.append(val)
        else:
            self.min.append(val)

    def pop(self) -> None:
        self.struct.pop()
        self.min.pop()

    def top(self) -> int:
        return self.struct[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()