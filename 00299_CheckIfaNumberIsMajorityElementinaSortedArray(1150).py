# 1150. Check If a Number Is Majority Element in a Sorted Array

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums) / 2