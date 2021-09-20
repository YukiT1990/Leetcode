# 937. Reorder Data in Log Files

# Reference
# https://leetcode.com/problems/reorder-data-in-log-files/discuss/779319/Python-Custom-Sort-Solution-With-Explanation

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         def sorting_algorithm(log):
#             left_side, right_side = log.split(" ", 1)

#             if right_side[0].isalpha():
#                 return (0, right_side, left_side)
#             else:
#                 return (1,)

#         return sorted(logs, key=sorting_algorithm)
    
        def sorting_algorithm(log):
            if log[-1].isnumeric():
                return (1,)
			
            left_side, right_side = log.split(" ", 1)
            return (0, right_side, left_side)

        return sorted(logs, key=sorting_algorithm)