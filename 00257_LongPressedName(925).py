# 925. Long Pressed Name

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while i < len(typed) and j < len(name):
            if typed[i] == name[j]:
                c = name[j]
                count_n = 0
                count_t = 0
                while typed[i] == c:
                    i += 1
                    if i == len(typed):
                        break
                    count_t += 1
                while name[j] == c:
                    j += 1
                    if j == len(name):
                        break
                    count_n += 1
                if count_n > count_t:
                    return False
            else:
                return False
            
        if i == len(typed) and j == len(name):
            return True
        else:
            return False
        