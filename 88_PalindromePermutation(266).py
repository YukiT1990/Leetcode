# 266. Palindrome Permutation

# 28 ms	14.1 MB
from collections import defaultdict, Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        letter_dict = {}
        for letter in s:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1
        if len(s) % 2 == 0:
            for value in letter_dict.values():
                if value % 2 == 1:
                    return False
            return True
        else:
            odd_count = 0
            for value in letter_dict.values():
                if value % 2 == 1:
                    odd_count += 1
                if odd_count > 1:
                    return False
            if odd_count == 0:
                return False
            return True
        
        # different solution
        # 28 ms	14 MB
#         sets = set()
#         for char in s:
#             if char not in sets:
#                 sets.add(char)
#             else:
#                 sets.remove(char)
        
#         return (len(sets) <= 1)    

# Reference to create dict from string
# https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-24.php