# 1119. Remove Vowels from a String

class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        for v in vowels:
            s = s.replace(v, '')
        return s