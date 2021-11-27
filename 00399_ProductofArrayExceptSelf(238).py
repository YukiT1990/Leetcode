# 238. Product of Array Except Self

# Reference
# https://leetcode.com/problems/product-of-array-except-self/discuss/927440/Python-no-division-time%3A-O(N)-space%3A-O(1)-(not-including-the-output-array)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]

        right_prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result
