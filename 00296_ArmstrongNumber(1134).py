# 1134. Armstrong Number

class Solution:
    def isArmstrong(self, n: int) -> bool:
        str_n = str(n)
        p = len(str_n)
        sum_n = 0
        for d in str_n:
            sum_n += int(d) ** p
        if sum_n == n:
            return True
        else:
            return False