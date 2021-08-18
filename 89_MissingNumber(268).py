# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            if nums[0] == 0:
                return 1
            else:
                return 0
        nums = sorted(nums)
        # print(nums)
        if nums[0] != 0:
                return 0
        for i in range(1, nums_len):
            if nums[i] - nums[i - 1] > 1:
                return i
        
        return nums_len
    
        # different answer
        # return sum(range(len(nums)+1)) - sum(nums)