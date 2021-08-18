# 252. Meeting Rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 64 ms	17.4 MB
        intervals = sorted(intervals)
        # 72 ms	17.6 MB
        # intervals = sorted(intervals, key=operator.itemgetter(0))
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True
        