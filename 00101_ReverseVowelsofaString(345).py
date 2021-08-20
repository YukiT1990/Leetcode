# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        # 428 ms	15.6 MB

        # if len(s) < 2:
        #     return s
        # vowel_list = []
        # for i in range(len(s)):
        #     if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        #         vowel_list.append(s[i])
        #         s = s[:i] + s[i:i+1].replace(s[i], '_') + s[i+1:]
        # if len(vowel_list) < 1:
        #     return s
        # vowel_list.reverse()
        # j = 0
        # for i in range(len(s)):
        #     if s[i] == '_':
        #         # s[i] = vowel_list[j]
        #         s = s[:i] + s[i:i+1].replace(s[i], vowel_list[j]) + s[i+1:]
        #         j += 1
        #         if j == len(vowel_list):
        #             break
        # return s
    

        # Reference
        # https://leetcode.com/problems/reverse-vowels-of-a-string/discuss/806132/99-faster-simplest-solution
        # 44 ms	15.1 MB
        vowels = set({"a", "e", "i", "o","u","A","E","I","O","U"})
        s = list(s)
        i,j = 0, len(s) - 1
        while i<j:
            if s[i] not in vowels and s[j] not in vowels:
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i = i + 1
                j = j - 1
            elif s[i] in vowels and s[j] not in vowels:
                j = j - 1
            else:
                i = i + 1
        return ''.join(s)
        