# 1015. Smallest Integer Divisible by K

# Reference
# https://leetcode.com/problems/smallest-integer-divisible-by-k/discuss/1655649/Python3-Less-Math-More-Intuition-or-2-Accepted-Solutions-or-Intuitive

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not k % 2 or not k % 5:
            return -1
        r = length = 1
        while True:
            r = r % k
            if not r:
                return length
            length += 1
            r = 10*r + 1
