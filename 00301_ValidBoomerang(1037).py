# 1037. Valid Boomerang

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        points = sorted(points, key=lambda x: x[1])
        points = sorted(points, key=lambda x: x[0])
        # print(points)
        if points[1][1] == points[0][1] and points[1][0] == points[0][0] or points[2][1] == points[1][1] and points[2][0] == points[1][0]:
            return False
        elif points[2][1] == points[1][1] and points[1][1] == points[0][1] or points[2][0] == points[1][0] and points[1][0] == points[0][0]:
            return False
        elif points[1][1] != points[0][1] and points[1][0] == points[0][0] or points[2][1] != points[1][1] and points[2][0] == points[1][0]:
            return True
        if (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) == (points[2][1] - points[1][1]) / (points[2][0] - points[1][0]):
            return False
        return True