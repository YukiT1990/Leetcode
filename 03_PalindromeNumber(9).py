# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        stringX = str(x)
        reverseStringX = stringX[::-1]
        if stringX == reverseStringX:
            return True
