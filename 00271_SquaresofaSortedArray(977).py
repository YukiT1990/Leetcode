# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def power2(n):
            return n ** 2
        
        powered = list(map(power2, nums))
        powered.sort()
        return powered