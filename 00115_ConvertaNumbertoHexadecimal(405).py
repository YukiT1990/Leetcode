# 405. Convert a Number to Hexadecimal

class Solution:
    def toHex(self, num: int) -> str:
        hexa = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num == 0: 
            return '0'
        if num < 0:
            num += 2 ** 32
        
        reversed_number = ""
        while num > 0:
            remainder = num % 16
            num -= remainder
            num //= 16
            reversed_number += str(hexa[remainder])

        return reversed_number[::-1]