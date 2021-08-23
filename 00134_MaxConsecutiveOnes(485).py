# 485. Max Consecutive Ones

# Reference
# https://leetcode.com/problems/max-consecutive-ones/discuss/711867/Python-one-liner-simple

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # inout [1,1,0,1,1,1]
        # print("".join(list(map(str, nums)))) 110111
        # print(list(map(len, ("".join(list(map(str, nums)))).split('0'))))  [2, 3]
        return max(list(map(len, ("".join(list(map(str, nums)))).split('0'))))