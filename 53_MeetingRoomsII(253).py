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


"""
Plus

253. Meeting Rooms II
Medium

4197

75

Add to List

Share
Given an array of meeting time intervals intervals
where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
Accepted
468K
Submissions
977.2K


"""
