# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
        stringX = str(abs(x))
        reversedStringX = stringX[::-1]
        reversedX = int(reversedStringX)
        if reversedX < -2**31 or reversedX > 2**31 - 1:
            return 0
        if isNegative:
            return -1 * reversedX
        return reversedX
