# 414. Third Maximum Number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        nums = sorted(nums, reverse = True)
        appeared = set()
        for i in range(len(nums)):
            appeared.add(nums[i])
            if len(appeared) == 3:
                return nums[i]
        