# 645. Set Mismatch

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ideal_sum = sum([x for x in range(1, len(nums) + 1)])
        real_sum = sum(nums)
        sum_without_absent = sum(set(nums))
        # print(ideal_sum)
        # print(real_sum)
        # print(sum_without_absent)
        diff = real_sum - ideal_sum
        absent_num = ideal_sum - sum_without_absent
        return [absent_num + diff, absent_num]
    
        # Reference
        # https://leetcode.com/problems/set-mismatch/discuss/1089519/Python.-faster-than-99.50-O(n)-time.-3-lines.-Explain.-math.-Super-simple.
        # l, s = len(nums), sum(set(nums))
        # ideal_sum = l * ( 1 + l ) // 2
        # return [sum(nums) - s, ideal_sum - s]
        
        # improved
        # length = len(nums)
        # ideal_sum = (1 + length) * length // 2
        # real_sum = sum(nums)
        # sum_without_absent = sum(set(nums))
        # return [real_sum - sum_without_absent, ideal_sum - sum_without_absent]