# 522. Longest Uncommon Subsequence II

# Reference
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/380412/Solution-in-Python-3-(beats-~100)

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        C = collections.Counter(strs)
        # print(C)  # Counter({'aba': 1, 'cdc': 1, 'eae': 1})
        strs = sorted(C.keys(), key = len, reverse = True)
        # print(strs)  # ['aba', 'cdc', 'eae']
        for i, s in enumerate(strs):
            if C[s] != 1: 
                continue
            b = True
            for j in range(i):
                I, c = -1, True
                for k in s:
                    I = strs[j].find(k, I+1)
                    if I == -1:
                        c = False
                        break
                if c:
                    b = False
                    break
            if b: return len(s)
        return -1