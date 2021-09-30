# 1180. Count Substrings with Only One Distinct Letter

class Solution:
    def countLetters(self, s: str) -> int:
        # 36 ms	14.3 MB
        # if len(s) == 1:
        #     return 1
        # result = 0
        # i = 0
        # start = -1
        # count = 0
        # while i < len(s) - 1:
        #     if s[i] == s[i+1]:
        #         start = i
        #         while i < len(s) - 1 and s[i] == s[i+1]:
        #             i += 1
        #         i += 1
        #         count = i - start
        #         # print(count)
        #         result += count * (count + 1) // 2
        #         # print(result)
        #         if i == len(s) - 1:
        #             if s[i] != s[start]:
        #                 result += 1
        #                 break
        #     else:
        #         result += 1
        #         i += 1
        #         if i == len(s) - 1:
        #             result += 1
        #             break
        # return result
                
        
        # 28 ms	14 MB
        # Reference
        # https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/discuss/434251/Python-3-Easy-Math-Method-24ms-O(1)-Memory-with-Explanation-Beats-99.06
        S = ' '+ s + ' '
        total, count = 0, 1
        for i in range(1, len(S)-1):
            if S[i] != S[i-1]:
                count = 1
            else:
                count += 1 
            total += count
        return total