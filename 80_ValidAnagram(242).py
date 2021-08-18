# 242. Valid Anagram

from collections import defaultdict, Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}
        for letter in s:
            dict_s[letter] = dict_s.get(letter, 0) + 1
        for letter in t:
            dict_t[letter] = dict_t.get(letter, 0) + 1
        
        if len(dict_s) != len(dict_t):
            return False
        for key, value in dict_s.items():
            if not key in dict_t.keys() or dict_t[key] != value:
                return False
        return True
    
    # improved
    # Reference
    # https://leetcode.com/problems/valid-anagram/discuss/1061765/Python-one-liner
        # return sorted(s) == sorted(t)