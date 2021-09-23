# 1002. Find Common Characters

# Reference
# https://leetcode.com/problems/find-common-characters/discuss/1010839/Python-Solution

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return None
        else:
            freq = Counter(words[0])
            for i in range(1, len(words)):
                for key in freq:
                    freq[key] = min(freq[key], words[i].count(key))
            
            return freq.elements()
            