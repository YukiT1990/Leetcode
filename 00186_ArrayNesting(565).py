# 565. Array Nesting

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # 148 ms	36.8 MB
        count_max = 0
        appeared = set()
        def helper(nums: List[int], num: int, count: int):
            if nums[num] < len(nums):
                if nums[num] not in appeared:
                    appeared.add(nums[num])
                    count += 1
                    return helper(nums, nums[num], count)
                else:
                    return count
                
        for num in nums:
            count_max = max(count_max, helper(nums, num, 0))
            
        return count_max
    
        # 111 ms	16 MB
        # Reference
        # https://leetcode.com/problems/array-nesting/discuss/364272/Solution-in-Python-3-(beats-100)-(only-seven-lines)
        # S = {}
        # for i in range(len(nums)):
        #     if nums[i] == -1: continue
        #     m, a = 0, i
        #     while nums[a] != -1: nums[a], a, b, m = -1, nums[a], a, m + 1
        #     S[i] = m + S.pop(b, 0)
        # return max(S.values())