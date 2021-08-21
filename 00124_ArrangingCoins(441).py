# 441. Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # 1556 ms	16.7 MB
        # if n == 1:
        #     return 1
        # sum_rows = [0, 1]
        # for i in range(2, n + 1):
        #     required = sum_rows[i - 1] + i
        #     if required > n:
        #         return i - 1
        #     sum_rows.append(required)
        
        # mathematical solution
        # 28 ms	14.3 MB
        return (-1 + int(sqrt(1 + 8 * n))) // 2
        