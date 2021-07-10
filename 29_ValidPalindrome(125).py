# 125. Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''.join(ch for ch in s if ch.isalnum()).lower()
        if len(alphanum) <= 1:
            return True

        for i in range(len(alphanum) // 2 + 1):
            if alphanum[i] != alphanum[len(alphanum) - 1 - i]:

                return False

        return True
