# 1317. Convert Integer to the Sum of Two No-Zero Integers

# Reference
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/discuss/915654/Python3-100-faster-100-less-memory-(16ms-14.1mb)

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for x in range(1, n):
            for c in str(x):
                if c == '0':
                    break
            else:
                y = n - x
                for c in str(y):
                    if c == '0':
                        break
                else:
                    return [x, y]