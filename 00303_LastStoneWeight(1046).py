# 1046. Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            y = stones[0]
            x = stones[1]
            stones = stones[2:]
            if y > x:
                stones.append(y-x)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0