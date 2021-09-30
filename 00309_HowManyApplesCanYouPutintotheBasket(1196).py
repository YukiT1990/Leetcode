# 1196. How Many Apples Can You Put into the Basket

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight = sorted(weight)
        sum_weight = 0
        for i in range(len(weight)):
            if sum_weight + weight[i] <= 5000:
                sum_weight += weight[i]
            else:
                if i > 0:
                    return i
                else:
                    return 0
        return len(weight)