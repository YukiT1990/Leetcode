# 878. Nth Magical Number

# Reference
# https://leetcode.com/problems/nth-magical-number/discuss/1545825/Python3-binary-search

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # inclusion-exclusion principle
        ab = lcm(a, b)
        lo, hi = 0, n*min(a, b)
        while lo < hi:
            mid = lo + hi >> 1
            if mid//a + mid//b - mid//ab < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % 1_000_000_007
