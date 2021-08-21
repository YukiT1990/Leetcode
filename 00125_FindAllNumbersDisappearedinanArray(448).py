# 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 362 ms	26 MB
        n = len(nums)
        all_num = [x for x in range(1, n + 1)]
        return set(all_num).difference(set(nums))
    
        # 352 ms	22.2 MB
        # Reference
        # https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/1028043/Python-3-Lines-Beats-90-With-Comments
        # result = [i for i in range(0, len(nums)+1)] # build an array (0, 1, 2, 3, ..., n)
        # for i in nums: result[i] = 0 # we index this array, setting "found" elements to zero
        # return [i for i in result if i != 0] # we return results that aren't zero