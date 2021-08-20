# 346. Moving Average from Data Stream

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.max = size
        self.queue = deque()
        self.length = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.length < self.max:
            self.queue.append(val)
            self.length += 1
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum / self.length


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)