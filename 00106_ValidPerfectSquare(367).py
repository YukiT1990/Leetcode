# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 44 ms	14.3 MB
        i = 1
        while i <= num / i:
            if i * i == num:
                return True
            i += 1
        return False
    

        # Binary Search
        # Reference
        # https://leetcode.com/problems/valid-perfect-square/discuss/744406/Python3-or-Binary-Search-or-Straight-Forward
        # 32 ms	14 MB

        # l,h=0,num
        # while(l<=h):
        #     m=(l+h)//2
        #     if (m*m ==num):
        #         return True
        #     elif (m*m < num):
        #         l=m+1
        #     else:
        #         h=m-1
        # return False
        