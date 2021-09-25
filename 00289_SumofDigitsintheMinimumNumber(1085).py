# 1085. Sum of Digits in the Minimum Number

class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        min_str = str(min(nums))
        sum_min_d = 0
        for d in min_str:
            sum_min_d += int(d)
        if sum_min_d % 2 == 1:
            return 0
        else:
            return 1