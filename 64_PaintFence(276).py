# 276. Paint Fence

class Solution:
    def numWays(self, n: int, k: int) -> int:
        array = [0, k, k * k]
        while len(array) <= n:
            array.append(array[-2] * (k - 1) + array[-1] * (k - 1))
        return array[n]
