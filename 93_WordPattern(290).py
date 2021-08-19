# 290. Word Pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        
        pat_dict = dict()
        
        for i in range(len(pattern)):
            if pattern[i] not in pat_dict.keys():
                pat_dict[pattern[i]] = s_list[i]
            else:
                if pat_dict[pattern[i]] != s_list[i]:
                    return False
        if len(set(pat_dict.keys())) != len(set(pat_dict.values())):
            return False
        return True