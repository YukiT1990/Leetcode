# 537. Complex Number Multiplication

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r_i_1 = num1.split('+')
        r_i_2 = num2.split('+')
        
        real_num = int(r_i_1[0]) * int(r_i_2[0]) - int(r_i_1[1][:len(r_i_1[1]) - 1]) * int(r_i_2[1][:len(r_i_2[1]) - 1])
        
        imaginary_num = int(r_i_1[0]) * int(r_i_2[1][:len(r_i_2[1]) - 1]) + int(r_i_2[0]) * int(r_i_1[1][:len(r_i_1[1]) - 1])
        
        return str(real_num) + '+' + str(imaginary_num) + 'i'