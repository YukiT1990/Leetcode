# 561. Array Partition I

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_min = 0
        for i in range(0, len(nums), 2):
            sum_min += nums[i]
        return sum_min

        # Different way (the same answer)
        # https://leetcode.com/problems/array-partition-i/discuss/671385/EASY-PYTHON-faster-than-95.81-two-lines
        # nums.sort()
        # return(sum(nums[::2]))