# 896. Monotonic Array

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] >= nums[-1]:
            for i in range(len(nums) - 1):
                if nums[i] < nums[i+1]:
                    return False
            return True
        elif nums[0] < nums[-1]:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    return False
            return True
                