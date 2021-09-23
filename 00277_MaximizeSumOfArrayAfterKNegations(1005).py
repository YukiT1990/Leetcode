# 1005. Maximize Sum Of Array After K Negations

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        # print(nums)
        
        if nums[0] >= 0:
            i = 0
            count = 0
            while count < k:
                nums[i] *= -1
                count += 1
        else:
            i = 0
            count = 0
            while count < k:
                nums[i] *= -1
                count += 1
                if len(nums) > i+1:
                    if nums[i+1] <= 0:
                        i += 1
                    elif nums[i+1] < nums[i]:
                        i += 1
                        
        # print(nums)
        return sum(nums)