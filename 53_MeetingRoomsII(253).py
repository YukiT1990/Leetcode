# 253. Meeting Rooms II

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        rooms = 0

        if not intervals:
            return 0

        endindex = 0

        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])

        for i in range(len(starts)):
            if starts[i] >= ends[endindex]:
                endindex += 1
            else:
                rooms += 1

        return rooms
        
