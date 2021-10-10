# 201. Bitwise AND of Numbers Range

# Reference
# https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/594259/100-memory-Python-3-One-line-(Short-with-Math)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return 0 if  right >= left*2 else functools.reduce(lambda x, y: x & y, range(left, right+1))