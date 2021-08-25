# 551. Student Attendance Record I

class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s or s.count('A') > 1:
            return False
        else:
            return True