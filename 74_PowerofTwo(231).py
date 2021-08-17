# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        while n != 1:
            if n % 2 == 0:
                n /= 2
                if n == 1:
                    return True
            else:
                return False
        
        # n(1)
        # Reference
        # https://leetcode.com/problems/power-of-two/discuss/948641/Python-O(1)-Solution
        # return n > 0 and n&(n - 1) == 0

        # When we have A & B == 0, it means that A and B have no common 1s, 
        # i.e. any two bits at the same positions of A and B are either different from each other, or two 0s.