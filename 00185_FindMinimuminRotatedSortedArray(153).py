# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 59 ms	14.5 MB
        # return min(nums) # this is accepted

        # 68 ms	14.6 MB
        # Reference
        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/758289/Clear-Python-3-solution-faster-than-93
        # left = 0
        # right = len(nums) - 1
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     num = nums[mid]
        #     if num > nums[right]:
        #         left = mid + 1
        #     elif mid == 0 or nums[mid - 1] > nums[mid]:
        #         return nums[mid]
        #     else:
        #         right = mid - 1

        # 47 ms	14.7 MB
        # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/1320815/Python-O(logn)-solution-using-binary-search
        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
        return nums[low]
        