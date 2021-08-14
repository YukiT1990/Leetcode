# 56. Merge Intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        output = []
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                output.append([start, end])
                start, end = interval[0], interval[1]
        output.append([start, end])
        return output
            
