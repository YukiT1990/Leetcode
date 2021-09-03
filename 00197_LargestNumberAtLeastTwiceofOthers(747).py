# 747. Largest Number At Least Twice of Others

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        index = nums.index(max(nums))
        nums.sort(reverse=True)
        if nums[0] >= nums[1] * 2:
            return index
        else:
            return -1