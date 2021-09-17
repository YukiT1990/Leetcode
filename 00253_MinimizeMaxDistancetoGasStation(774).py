# 774. Minimize Max Distance to Gas Station

# Reference
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/discuss/320839/Thoughts-and-Lessons-from-the-Max-Heap-Solution

import heapq
import math

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # priority queue
        # the lower bound of the solution is the entire length divided by (K+1)
        bound = (stations[-1] - stations[0]) / (k + 1)
        added = 0  # keeps track of the stations already built
        max_heap = []
        for i in range(1, len(stations)):
            needed = math.ceil((stations[i] - stations[i-1]) / bound) - 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1])/(needed+1), i, needed))
            added += needed
        
        while added < k:
            cur, i, needed = heapq.heappop(max_heap)
            needed += 1
            heapq.heappush(max_heap, (-(stations[i] - stations[i-1])/(needed+1), i, needed))
            added += 1
        
        return -max_heap[0][0]