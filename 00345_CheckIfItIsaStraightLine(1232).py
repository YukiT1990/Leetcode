# 1232. Check If It Is a Straight Line

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 60 ms	14.8 MB
        if len(coordinates) == 2:
            return True
        if coordinates[1][0] == coordinates[0][0]:
            for i in range(len(coordinates) - 1):
                if coordinates[i+1][0] != coordinates[i][0]:
                    return False
            return True
        if coordinates[1][1] == coordinates[0][1]:
            for i in range(len(coordinates) - 1):
                if coordinates[i+1][1] != coordinates[i][1]:
                    return False
            return True
        
        a = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        b = coordinates[0][1] - a * coordinates[0][0]
        for x, y in coordinates:
            if y != x * a + b:
                return False
        return True
    
    
        # 48 ms	14.6 MB
        # Reference
        # https://leetcode.com/problems/check-if-it-is-a-straight-line/discuss/620096/Java-Python3-CPP-or-Simple-code-with-explanation-or-100-fast-or-O(1)-space
        # (x1, y1), (x2, y2) = coordinates[:2]
        # for i in range(2, len(coordinates)):
        #     (x, y) = coordinates[i]
        #     if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
        #         return False
        # return True	