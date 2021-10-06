# 1957. Delete Characters to Make Fancy String

# Reference
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/discuss/1389309/This-my-simple-solution

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        result = s[:2]
        for i in range(2, len(s)):
            if result[-1] != s[i] or result[-2] != s[i]:
                result += s[i]
        return result
    