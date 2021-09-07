# 812. Largest Triangle Area

# Reference
# https://leetcode.com/problems/largest-triangle-area/discuss/333629/Two-Solutions-in-Python-3-(Shoelace-Method-and-Heron's-Formula)

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def Area_Shoelace(a,b,c):
	        return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1]))/2
    
        L, A = len(points), 0
        for i in range(L-2):
            for j in range(i+1, L-1):
                for k in range(j+1, L):
                    R = Area_Shoelace(points[i], points[j], points[k])
                    A = max(A, R)
        return A
    