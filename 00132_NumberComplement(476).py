# 476. Number Complement

class Solution:
    def findComplement(self, num: int) -> int:
        # 32 ms	14.3 MB
        # bin_n = "{0:b}".format(num)
        # result = ""
        # for d in bin_n:
        #     if d == '1':
        #         result += '0'
        #     else:
        #         result += '1'
        # return int(result, 2)
    
        # 24 ms	14.3 MB
        bin_n = "{0:b}".format(num)
        result = 0
        for i in range(len(bin_n)):
            # complement
            if bin_n[i] == '0':
                result += 2**(len(bin_n) - i - 1)
        return result