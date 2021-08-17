# 303. Range Sum Query - Immutable

class NumArray:

#     def __init__(self, nums: List[int]):
#         self.array = nums

#     def sumRange(self, left: int, right: int) -> int:
#         sumR = 0
#         for i in range(left, right + 1):
#             sumR += self.array[i]
#         return sumR

# improved
# Reference
# https://leetcode.com/problems/range-sum-query-immutable/discuss/597654/Easy-to-Understand-or-Faster-or-Simple-or-Python-Solution

    def __init__(self, nums: List[int]):
        self.sum = []
        sum_till = 0
        for i in nums:
            sum_till += i
            self.sum.append(sum_till)

    def sumRange(self, left: int, right: int) -> int:
        if left > 0 and right > 0:
            return self.sum[right] - self.sum[left - 1]
        else:
            return self.sum[left or right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)