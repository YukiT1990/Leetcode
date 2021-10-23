# 154. Find Minimum in Rotated Sorted Array II

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 63 ms	14.6 MB
        # return min(nums)

        # 59 ms	14.9 MB
        min_num = nums[0]
        for i in range(len(nums) - 1):
            if nums[i+1] < nums[i]:
                min_num = nums[i+1]
                break
        return min_num
    