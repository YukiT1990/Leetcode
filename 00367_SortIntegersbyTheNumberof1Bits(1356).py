# 1356. Sort Integers by The Number of 1 Bits

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr = sorted(arr, key=lambda x: bin(x)[2:].count('1'))
        return arr

        # one line
        # Reference
        # https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/submissions/
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))