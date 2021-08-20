# 383. Ransom Note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # 60 ms	14.7 MB
        ransomNote = list(ransomNote.strip())
        magazine = list(magazine.strip())
        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True
    
        # Reference
        # https://leetcode.com/problems/ransom-note/discuss/704431/python-3-easy-solution-faster-than-93
        # 32 ms	14.2 MB
        # for c in set(ransomNote):
        #     if magazine.count(c) < ransomNote.count(c):
        #         return False
        # return True