# 961. N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # 212 ms	15.6 MB
        for num in nums:
            if nums.count(num) == len(nums) // 2:
                return num

        # 200 ms	15.7 MB
        # Reference
        #  https://leetcode.com/problems/n-repeated-element-in-size-2n-array/discuss/1337509/PYTHON-3-%3A-SUPER-EASY-99.52-FASTER
        # list1 = []
        # for num in nums :
        #     if num in list1 :
        #         return num
        #     else :
        #         list1.append(num)