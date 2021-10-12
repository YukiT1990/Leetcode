# 1332. Remove Palindromic Subsequences

# Reference
# https://leetcode.com/problems/remove-palindromic-subsequences/discuss/490902/Python3-sneaky-definition-of-%22subsequence%22

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        if s == s[::-1]:
            return 1
        return 2
            