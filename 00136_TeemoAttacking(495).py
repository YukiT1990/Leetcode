# 495. Teemo Attacking

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        seconds = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration - 1 >= timeSeries[i + 1]:
                seconds += (timeSeries[i + 1] - timeSeries[i])
            else:
                seconds += duration
        seconds += duration
        return seconds