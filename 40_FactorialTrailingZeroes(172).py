# 172. Factorial Trailing Zeroes

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # In mathematics, trailing zeros are a sequence of 0 in the decimal representation (or more generally, in any positional representation) of a number, after which no other digits follow.
        # The number of the occurrence of maltiples of 2 is greater than the number of the occurrence of maltiples of 5 in the n items of n!.
        # The quotient of n // 5 means that there are n // 5 of maltiples of 5 in the n items of n!.
        # Hence, the number of the occurrence of maltiples of 5 in the n items of n! means that the number of the occurrence of maltiples of 10 in the n items of n!.
        # Which means that the number of trailing zeros.
        # In the next recursion, n // 5 means that the number of the occurrence of maltiples of 25 in the n items of n! and so on.


        quotient = n // 5
        return quotient + self.trailingZeroes(quotient) if quotient >= 5 else quotient
