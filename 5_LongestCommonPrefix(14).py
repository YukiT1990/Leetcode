# 14. Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        i = 0
        minWordLength = 200
        for word in strs:
            if len(word) < minWordLength:
                minWordLength = len(word)
        while i < minWordLength:
            char = strs[0][i]
            for word in strs:
                if word[i] == char:
                    continue
                else:
                    return result
            result = result + char
            i += 1
        return result
