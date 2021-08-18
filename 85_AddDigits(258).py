# 258. Add Digits

class Solution:
    def addDigits(self, num: int) -> int:
        
        def helper(num: int) -> int:
            str_num = str(num)
            sum_num = 0
            for d in str_num:
                sum_num += int(d)
            return sum_num
        
        while len(str(num)) > 1:
            num = helper(num)
            
        return num
        