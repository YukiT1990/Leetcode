# 1413. Minimum Value to Get Positive Step by Step Sum

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        smallest = 100
        cur_sum = 0
        for num in nums:
            cur_sum += num
            smallest = min(smallest, cur_sum)
        if smallest < 0:
            return smallest * (-1) + 1
        else:
            return 1
