# 246. Strobogrammatic Number

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        left = 0
        right = len(num) - 1
        
        while left <= right:
            if num[left] in ['2', '3', '4', '5', '7']:
                return False
            elif num[left] in ['0', '1', '8'] and num[left] != num[right]:
                return False
            elif num[left] == '6' and num[right] != '9' or num[left] == '9' and num[right] != '6':
                return False
            left += 1
            right -= 1
        return True
        