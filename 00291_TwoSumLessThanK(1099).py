# 1099. Two Sum Less Than K

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            if nums[i] <= k:
                nums = nums[i:]
                break
        # print(nums)
        result = -1
        if len(nums) < 2:
            return result
        left = 0
        right = len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp < k:
                right -= 1
                result = max(result, temp)
            else:
                left += 1
        return result
