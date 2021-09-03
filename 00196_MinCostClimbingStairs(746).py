# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_cost = [0, 0]
        for i in range(len(cost) - 1):
            total_cost.append(min(total_cost[i] + cost[i], total_cost[i+1] + cost[i+1]))
        # print(total_cost)
        return total_cost[-1]