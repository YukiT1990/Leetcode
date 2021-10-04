# 1331. Rank Transform of an Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # arr_set = list(set(arr))
        # arr_set.sort()
        # # print(arr_set)
        # arr_dict = dict()
        # result = []
        # for num in arr:
        #     if num not in arr_dict.keys():
        #         arr_dict[num] = arr_set.index(num)+1
        #     result.append(arr_dict[num])
        # return result
    
        # Reference
        # https://leetcode.com/problems/rank-transform-of-an-array/discuss/492212/Python-3-(two-lines)-(beats-~100)
        D = {j: i+1 for i,j in enumerate(sorted(set(arr)))}
        return map(D.get, arr)