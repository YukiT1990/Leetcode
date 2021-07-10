# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        integer_sum = int(a, 2) + int(b, 2)
        binary_sum = str(bin(integer_sum))
        return binary_sum[2:]
