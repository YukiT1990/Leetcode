# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        basket = set()
        basket.add(n)

        str_n = str(n)

        def sumOfSquareOfDigits(str_num):
            sumN = 0
            for char in str_num:
                sumN += int(char) ** 2
            return sumN

        while True:
            if sumOfSquareOfDigits(str_n) == 1:
                return True
            else:
                new_n = sumOfSquareOfDigits(str_n)
                if new_n in basket:
                    return False
                else:
                    basket.add(new_n)
                    str_n = str(new_n)
