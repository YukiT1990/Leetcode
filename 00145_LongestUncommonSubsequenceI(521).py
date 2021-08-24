# 521. Longest Uncommon Subsequence I

# Reference 
# https://leetcode.com/problems/longest-uncommon-subsequence-i/discuss/380325/Solution-in-Python-3-(beats-~90)-(one-line)

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))