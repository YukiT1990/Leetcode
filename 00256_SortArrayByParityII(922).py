# 922. Sort Array By Parity II

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 297 ms	16.7 MB
        result = [0 for _ in range(len(nums))]
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        for i in range(len(nums) // 2):
            result[i*2] = evens[i]
            result[i*2+1] = odds[i]
            
        return result
    
    
        # 216 ms	16.2 MB
        # Reference
        # https://leetcode.com/problems/sort-array-by-parity-ii/discuss/1330742/Two-Pointer-Solution-or-Python-3-or-beats-90
#         e = 0 #even_index
#         o = 1 #odd_index
        
#         while e<len(nums) and o<len(nums):
#             if nums[e]%2==0:
#                 e+=2
#             else:
#                 if nums[o]%2!=0:
#                     o+=2
#                 else:
#                     nums[e],nums[o] = nums[o],nums[e]
#                     e+=2
#                     o+=2
                                
#         return nums