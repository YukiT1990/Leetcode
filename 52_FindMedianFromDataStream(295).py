# 295. Find Median from Data Stream

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        n = len(self.array)
        if n % 2 == 0:
            return (self.array[n // 2 - 1] + self.array[n // 2]) / 2.0
        else:
            return self.array[n // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
