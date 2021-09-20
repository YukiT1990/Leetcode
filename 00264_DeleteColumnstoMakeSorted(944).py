# 944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # 252 ms	15.6 MB
        result = 0
        array2d = [[0 for _ in range(len(strs))] for _ in range(len(strs[0]))]
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                array2d[j][i] = strs[i][j]
        for i in range(len(array2d)):
            sortedarray2da = sorted(array2d[i])
            str_array2d = ''.join(array2d[i])
            str_sortedarray2da = ''.join(sortedarray2da)
            if str_array2d != str_sortedarray2da:
                result += 1
        return result
        
        # 77 ms	15 MB
        # Reference
        # https://leetcode.com/problems/delete-columns-to-make-sorted/discuss/382127/Solution-in-Python-3-(beats-~100)-(one-line)
        # return sum(list(i) != sorted(i) for i in zip(*strs))