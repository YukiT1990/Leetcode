# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        i = 0
        carry_up = False
        result = ""
        while i < len(num1) or i < len(num2):
            temp_sum = 0
            if i < len(num1) and i < len(num2):
                temp_sum += int(num1[i]) + int(num2[i])
            elif i < len(num1):
                temp_sum += int(num1[i])
            elif i < len(num2):
                temp_sum += int(num2[i])
            if carry_up:
                temp_sum += 1
            if temp_sum > 9:
                carry_up = True
            else:
                carry_up = False
            str_sum = str(temp_sum)
            result += str_sum[-1]
            i += 1

        if carry_up:
            result += '1' 
            
        return result[::-1]
    
        # Different answer
        # Reference
        # https://leetcode.com/problems/add-strings/discuss/734968/Simple-python-solution
        
        # def str2int(num):
        #     numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
        #           '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        #     output = 0
        #     for d in num:
        #         output = output * 10 + numDict[d]
        #     return output
        
        # return str(str2int(num1) + str2int(num2)) 
        