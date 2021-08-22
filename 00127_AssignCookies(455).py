# 455. Assign Cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 168 ms	15.9 MB
        if len(s) == 0:
            return 0
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)
        content_children = 0
        j = 0
        for i in range(len(s)):
            while s[i] < g[j] and j < len(g) - 1:
                j += 1
            if s[i] >= g[j]:
                content_children += 1
                j += 1
                if j >= len(g):
                    break
        return content_children
    
        # 148 ms	16 MB
        # Reference
        # https://leetcode.com/problems/assign-cookies/discuss/355290/Faster-than-100
        # if not g or not s:
        #     return 0
        # g.sort()
        # s.sort()
        # res = 0
        # child_i = 0 
        # for cake in s:
        #     if child_i >= len(g):
        #         return res
        #     if cake >= g[child_i]:
        #         res += 1
        #         child_i += 1
        
        # return res