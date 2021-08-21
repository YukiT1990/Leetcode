# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_dict = {}
        for letter in s:
            word_dict[letter] = word_dict.get(letter, 0) + 1
            
        even_sum = 0
        exist_odd = False
        
        for value in word_dict.values():
            if value % 2 == 0:
                even_sum += value
            else:
                if not exist_odd:
                    exist_odd = True
                even_sum += (value - 1)
             
        if exist_odd:
            even_sum += 1
            
        return even_sum
            