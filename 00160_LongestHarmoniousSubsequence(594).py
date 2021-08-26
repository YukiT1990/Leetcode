# 594. Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_dict = dict()
        
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            
        result = 0
        
        for key in num_dict.keys():
            if key + 1 in num_dict.keys():
                result = max(result, num_dict[key] + num_dict[key + 1])
        return result