# 170. Two Sum III - Data structure design

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []
        self.sorted = False

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.array.append(number)
        self.sorted = False


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if not self.sorted:
            self.array.sort()
        i, j = 0, len(self.array) - 1
        while i < j:
            if self.array[i] + self.array[j] > value:
                j = bisect_right(self.array, value - self.array[i], i + 1, j) - 1
            elif self.array[i] + self.array[j] < value:
                i = bisect_left(self.array, value - self.array[j], i + 1, j - 1)
            else:
                return True
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
