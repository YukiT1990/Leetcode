# 344. Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        # Different answer
        # Reference 
        # https://leetcode.com/problems/reverse-string/discuss/946287/Python-Easy-Solution
        
        # for i in range(len(s)//2):
        #     s[i],s[-i-1]=s[-i-1],s[i]
        # return s