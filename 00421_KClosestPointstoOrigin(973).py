# 973. K Closest Points to Origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # 3364 ms	19.9 MB
        dist_dict = {}
        dist_list = []

        for i in range(len(points)):
            dist = math.sqrt(points[i][0]**2 + points[i][1]**2)
            dist_dict[i] = dist
            dist_list.append(dist)

        dist_list = sorted(dist_list)
        dist_list = dist_list[:k]
        result = [points[i]
                  for i in range(len(points)) if dist_dict[i] in dist_list]
        return result
