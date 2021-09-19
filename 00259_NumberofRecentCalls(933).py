# 933. Number of Recent Calls

class RecentCounter:

    def __init__(self):
        self.count = []

    def ping(self, t: int) -> int:
        self.count.append(t)
        i = 0
        while i < len(self.count):
            if self.count[i] >= t - 3000:
                break
            if self.count[i] < t - 3000:
                self.count.pop(i)
            else:
                i += 1
        return len(self.count)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)