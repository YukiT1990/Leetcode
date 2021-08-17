# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return nums
        
        result = []
        
        start, end = nums[0], nums[0]
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or ((i < len(nums) - 1) and (nums[i + 1] > nums[i] + 1)):
                end = nums[i]
                
                if start != end:
                    result.append(str(start) + "->" + str(end))
                else:
                    result.append(str(start))
                    
                if i < len(nums) - 1:
                    start, end = nums[i + 1], nums[i + 1] 
                
        return result