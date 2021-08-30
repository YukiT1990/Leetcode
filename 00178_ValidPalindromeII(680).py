# 680. Valid Palindrome II

# Reference
# https://leetcode.com/problems/valid-palindrome-ii/discuss/632647/Python-Readable-and-Intuitive-Solution-(Generalizable-to-n-deletes)

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def verify(s, left, right, deleted):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    else:
                        return verify(s, left+1, right, True) or verify(s, left, right-1, True)
                else:
                    left += 1
                    right -= 1
            return True
        return verify(s, 0, len(s)-1, False)