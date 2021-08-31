# 716. Max Stack

from collections import deque

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque([])
        self.list = []
        self.max_val = -1 * 10 ** 7

    def push(self, x: int) -> None:
        self.max_val = max(self.max_val, x)
        self.stack.appendleft(x)
        self.list.append(x)

    def pop(self) -> int:
        x = self.stack[0]
        self.list.remove(x)
        if len(self.list) > 0:
            if self.max_val == x:
                self.max_val = max(self.list)
        else:
            self.max_val = -1 * 10 ** 7
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def peekMax(self) -> int:
        return self.max_val

    def popMax(self) -> int:
        x = self.max_val
        self.list.remove(x)
        self.stack.remove(x)
        if len(self.list) > 0:
            self.max_val = max(self.list)
        else:
            self.max_val = -1 * 10 ** 7
        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()