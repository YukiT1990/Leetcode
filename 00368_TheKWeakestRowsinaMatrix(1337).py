# 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weakest_num = len(mat[0])
        weakest_rows = []
        for i in range(len(mat)):
            temp = mat[i].count(1)
            if temp < weakest_num:
                weakest_num = temp
        while len(weakest_rows) < k:
            for i in range(len(mat)):
                temp = mat[i].count(1)
                if temp == weakest_num:
                    weakest_rows.append(i)
            weakest_num += 1
        return weakest_rows[:k]
        