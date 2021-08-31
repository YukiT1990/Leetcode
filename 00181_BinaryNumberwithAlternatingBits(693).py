# 693. Binary Number with Alternating Bits

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # 64 ms	14.1 MB
        bin_num = bin(n)[2:]
        # print(bin_num)
        for i in range(len(bin_num) - 1):
            if bin_num[i] == bin_num[i+1]:
                return False
        return True
    
        # 47 ms	14.1 MB
        # Reference
        # https://leetcode.com/problems/binary-number-with-alternating-bits/discuss/557292/Python3-Easy-understanding-solution-Beats-98.99
        # b = bin(n)[2:]
        # return all(int(b[i]) + int(b[i+1]) == 1 for i in range(len(b)-1))