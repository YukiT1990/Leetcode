# 260. Single Number III

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        i = 0
        result = []
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                result.append(nums[i])
                i += 1
        if i < len(nums) and nums[i] != nums[i-1]:
            result.append(nums[i])
        return result
