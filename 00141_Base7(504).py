# 504. Base 7

class Solution:
    def convertToBase7(self, num: int) -> str:
        remainders = []
        isNegative = False
        if num < 0:
            isNegative = True
            num *= -1
        while num >= 7:
            remainders.append(str(num % 7))
            num //= 7
        if num < 7:
            remainders.append(str(num))
        if isNegative:
            remainders.append('-')
        
        remainders.reverse()
        return ''.join(remainders)