# 739. Daily Temperatures

# Reference
# https://leetcode.com/problems/daily-temperatures/discuss/838903/Python%3A-O(n)-time-and-O(1)-space-(without-Stack)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days_count = len(temperatures)

        next_warm_day = [0 for _ in range(days_count)]

        for d in range(days_count - 2, -1, -1):

            next_day = 1
            # while next_node and next_node.val <= curr_node.val
            while next_day and temperatures[d + next_day] <= temperatures[d]:
                if next_warm_day[d + next_day]:
                    next_day += next_warm_day[d + next_day]

                else:
                    next_day = 0
            next_warm_day[d] = next_day

        return next_warm_day
