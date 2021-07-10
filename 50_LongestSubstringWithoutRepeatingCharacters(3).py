# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)
        lis = [0] * n

        i = 0
        while i < len(s):
            num = 0
            basket = set()
            for j in range(i, len(s)):
                if not s[j] in basket:
                    basket.add(s[j])
                    num += 1
                else:
                    break
            lis[i] = num
            i += 1

        return max(lis)
