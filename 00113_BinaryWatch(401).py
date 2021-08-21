# 401. Binary Watch

# Reference
# https://leetcode.com/problems/binary-watch/discuss/335057/Easy-Python3-solution

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn < 0 or turnedOn > 10:
            return []
        
        result = []
        
        for hour in range(0, 12):
            for minute in range(0, 60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    result.append('{:d}:{:02d}'.format(hour, minute))
                    
        return result