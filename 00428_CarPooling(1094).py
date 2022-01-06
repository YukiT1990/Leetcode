# 1094. Car Pooling

# Reference
# https://leetcode.com/problems/car-pooling/discuss/857862/Python-Simple-Solution-Explained-(video-%2B-code)

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []
        for ppl, start, end in trips:
            stops.append((start, ppl))
            stops.append((end, -ppl))
        
        stops.sort()
        
        for _, ppl in stops:
            capacity -= ppl
            if 0 > capacity:
                return False
        return True