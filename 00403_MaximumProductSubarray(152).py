# 152. Maximum Product Subarray

# Reference
# https://leetcode.com/problems/maximum-product-subarray/discuss/841169/Python-3-or-DP-or-Explanations

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # case are handled differently depends on whether current number is positive or negative
        ans, cur_max, cur_min = -sys.maxsize, 0, 0
        for num in nums:
            if num > 0:
                cur_max, cur_min = max(num, num*cur_max), min(num, num*cur_min)
            else:
                cur_max, cur_min = max(num, num*cur_min), min(num, num*cur_max)
            ans = max(ans, cur_max)
        return ans if ans else max(nums)
