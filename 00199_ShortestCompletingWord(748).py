# 748. Shortest Completing Word

# Reference
# https://leetcode.com/problems/shortest-completing-word/discuss/351082/Solution-in-Python-3-(beats-100)

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        L, i, m = Counter([i for i in licensePlate.lower() if i.isalpha()]), 0, float('inf')
        S = set(L)
        words = [i for i in words if S.issubset(set(i))]
        while i < len(words):
            if len(words[i]) >= m:
                del words[i]
                continue
            A = Counter(words[i])
            for j in L:
                if L[j] > A[j]:
                    del words[i]
                    i -= 1
                    break
                if j == list(L)[-1] and len(words[i]) < m:
                    m = len(words[i])
            i += 1
        return words[-1]