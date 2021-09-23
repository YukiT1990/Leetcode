# 1009. Complement of Base 10 Integer

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = bin(n)[2:]
        complement = ''
        for d in binary:
            if d == '0':
                complement += '1'
            else:
                complement += '0'
        return int(complement, 2)