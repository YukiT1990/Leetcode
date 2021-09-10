# 859. Buddy Strings

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(s) == len(set(s)):
                return False
            else:
                return True
        s = list(s.strip())
        goal = list(goal.strip())
        
        indexes = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                indexes.append(i)
                if len(indexes) > 2:
                    return False
        
        if len(indexes) == 1:
            return False
        s[indexes[0]], s[indexes[1]] = s[indexes[1]], s[indexes[0]]
        
        if s == goal:
            return True
        else:
            return False