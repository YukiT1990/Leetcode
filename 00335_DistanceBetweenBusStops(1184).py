# 1184. Distance Between Bus Stops

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        dist1 = 0
        dist2 = 0
        whole_route = sum(distance)
        if start < destination:
            small = start
            large = destination
        else:
            small = destination
            large = start
            
        for i in range(small, large):
            dist1 += distance[i]
        dist2 = whole_route - dist1
        return min(dist1, dist2)
    
        # Reference
        # https://leetcode.com/problems/distance-between-bus-stops/discuss/377844/Python-Explanation
        # a, b = min(start, destination), max(start, destination)
        # return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))
        