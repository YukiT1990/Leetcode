# 1021. Remove Outermost Parentheses

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
          # 52 ms	14.8 MB
#         indexes = []
#         stack = []
#         for i in range(len(s)):
#             if len(stack) == 0:
#                 if i > 0:
#                     indexes.append(i-1)
#                 indexes.append(i)
#             if s[i] == '(':
#                 stack.append('(')
#             if s[i] == ')':
#                 stack.pop()
                
#         indexes.append(len(s)-1)
#         # print(indexes)
#         s = list(s.strip())
#         indexes.reverse()
#         for i in indexes:
#             s.pop(i)
#         return ''.join(s)
    
        # 32 ms	14.4 MB
        # Reference
        # https://leetcode.com/problems/remove-outermost-parentheses/discuss/594405/Python-Super-Easy-98-Speed
        popen, result = 0, []
        for x in s:
            if x==')':
                popen -= 1
            if popen>0:
                result.append(x)
            if x=='(':
                popen += 1
        return ''.join(result)
                