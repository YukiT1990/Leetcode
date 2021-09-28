# 1133. Largest Unique Number

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        i = 0
        while i < len(nums):
            # 76 ms	14.5 MB	
            # count = nums.count(nums[i])
            # if count == 1:
            #     return nums[i]
            # else:
            #     i += count
            
            # 48 ms	14.5 MB
            if i < len(nums) - 1:
                if nums[i] > nums[i+1]:
                    return nums[i]
                else:
                    current = nums[i]
                    while nums[i] == current:
                        i += 1
                        if i == len(nums):
                            break
            else:
                return nums[i]
        return -1