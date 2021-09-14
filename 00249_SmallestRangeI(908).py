# 908. Smallest Range I

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums)
        if diff <= k * 2:
            return 0
        else:
            return diff - k * 2
        
        # one line
        # return max(0, max(nums) - min(nums) - k * 2)