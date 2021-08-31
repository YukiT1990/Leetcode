# 697. Degree of an Array

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 9723 ms	15.6 MB
#         dict_num = {}
#         for num in nums:
#             dict_num[num] = dict_num.get(num, 0) + 1
#         max_nums = []
#         max_val = max(dict_num.values())
#         for k, v in dict_num.items():
#             if v == max_val:
#                 max_nums.append(k)
#         min_len = len(nums)
#         for max_num in max_nums:
#             left = 0
#             right = len(nums) - 1
            
#             while left <= right:
#                 if nums[left] != max_num:
#                     left += 1
#                 if nums[right] != max_num:
#                     right -= 1
#                 if nums[left] == max_num and nums[right] == max_num:
#                     break
                    
#             min_len = min(min_len, right - left + 1)
#         return min_len
    
        # Reference
        # https://leetcode.com/problems/degree-of-an-array/discuss/748298/Easy-Python-or-One-Pass-or-3-Approaches-or-Top-Speed

        # 340 ms	16.8 MB
        # # Group indexes by element type
        # d = defaultdict(list)
        # for i,x in enumerate(nums):
        #     d[x].append(i)
        # #
        # # Find highest Degree
        # m = max([ len(v) for v in d.values() ])
        # #
        # # Find shortest span for max. degree
        # best = len(nums)
        # for v in d.values():
        #     if len(v)==m:
        #         best = min(best,v[-1]-v[0]+1)
        # return best
    

        # 430 ms	16.6 MB
        # d       = defaultdict(list) # Dictionary with [indexes] where each label appears
        # m, best = 1, 1              # m = record degree, best = shortest span (for m)
        # for i,x in enumerate(nums):
        #     d[x].append(i) # Add index to respective sub-array
        #     L =len(d[x])   # Track length of sub-array at label = x
        #     if L>m:
        #         # Initialize new Record
        #         m = L
        #         best = i - d[x][0] + 1
        #     elif L == m:
        #         # Pick best at highest degree
        #         best = min( best , i - d[x][0] + 1 )
        # return best
    

        # 252 ms	15.7 MB
        d       = {}    # Dictionary with information for each label x = nums[i]
        #                 Entries have the form d[x] = [i, m] = [beginning_subarray, degree]
        #
        A, best = 1, 1  # A = record degree, best = shortest span (for A)
        #
        for i,x in enumerate(nums):
            if x in d:
                d[x][1] += 1               # Update Degree
                m        = d[x][1]         # Fetch Degree
                L        = i - d[x][0] + 1 # Length sub-array
            else:
                d[x] = [i,1]
                L    = m = 1
            if m>A:
                # Initialize new Record
                A,best = m, L
            elif A == m:
                # Pick best at highest degree
                best = min( best , L )
        return best