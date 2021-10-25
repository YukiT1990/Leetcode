# 155. Min Stack

class MinStack:

    # 592 ms 18.2 MB
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        if self.items:
            return min(self.items)
        else:
            return None

    # 70 ms	18 MB
    def __init__(self):
        self.stack = []
        self.man_val = 2 ** 31 - 1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.man_val = min(self.man_val, val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.man_val:
                if len(self.stack[:-1]) > 0:
                    self.man_val = min(self.stack[:-1])
                else:
                    self.man_val = 2 ** 31 - 1
            self.stack = self.stack[:-1]

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return self.man_val
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
