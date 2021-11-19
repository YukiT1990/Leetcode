# 461. Hamming Distance

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 24 ms	13.9 MB
        bin_x = bin(x)[2:][::-1]
        bin_y = bin(y)[2:][::-1]
        len_x = len(bin_x)
        len_y = len(bin_y)
        
        diff = 0
        if len_x - len_y >= 0:
            bin_y += '0' * (len_x - len_y)
        else:
            bin_x += '0' * (len_y - len_x)
        
        for i in range(len(bin_x)):
            if bin_x[i] != bin_y[i]:
                diff += 1
            
        return diff

            


        # 50 ms	14.3 MB
        # count = 0
        # bin_r_x = bin(x)[2:][::-1]
        # bin_r_y = bin(y)[2:][::-1]
        # if len(bin_r_x) <= len(bin_r_y):
        #     for i in range(len(bin_r_x)):
        #         if bin_r_x[i] != bin_r_y[i]:
        #             count += 1
        #     for d in bin_r_y[len(bin_r_x):]:
        #         if d == '1':
        #             count += 1
        # else:
        #     for i in range(len(bin_r_y)):
        #         if bin_r_y[i] != bin_r_x[i]:
        #             count += 1
        #     for d in bin_r_x[len(bin_r_y):]:
        #         if d == '1':
        #             count += 1
        # return count
    
        # 42 ms	14.2 MB
        # Reference
        # https://leetcode.com/problems/hamming-distance/discuss/943245/python-3-28ms
        # return sum(1 for i in bin(x^y) if i == "1")
        # ^ means XOR
                