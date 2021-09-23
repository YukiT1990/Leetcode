# 1328. Break a Palindrome

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        if len(palindrome) == palindrome.count('a'):
            palindrome = 'a' * (len(palindrome) - 1) + 'b'
            return palindrome
        for i in range(len(palindrome) // 2 + 1):
            if i < len(palindrome) // 2:
                if palindrome[i] != 'a':
                    if i == 0:
                        palindrome = 'a' + palindrome[i+1:]
                    else:
                        palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                    return palindrome
            else:
                if palindrome[len(palindrome) // 2 + 1:].count('z') == len(palindrome[len(palindrome) // 2 + 1:]):
                    palindrome = palindrome[:len(palindrome) // 2] + chr(ord(palindrome[len(palindrome) // 2])+ 1) + palindrome[len(palindrome) // 2 + 1:]
                else:
                    palindrome = palindrome[:-1] + chr(ord(palindrome[-1])+ 1)
                
        return palindrome
        