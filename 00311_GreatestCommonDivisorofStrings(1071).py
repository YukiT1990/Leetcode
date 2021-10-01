# 1071. Greatest Common Divisor of Strings

# Reference
# https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/860984/Python-3-or-GCD-1-liner-or-Explanation

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 == str2 + str1:
            return str2[:math.gcd(len(str1), len(str2))]
        else:
            return ''
        