# 1323. Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        s_num = str(num)
        if '6' not in s_num:
            return num
        for i in range(len(s_num)):
            if s_num[i] == '6':
                s_num = s_num[:i] + '9' + s_num[i+1:]
                break
        return int(s_num)
            