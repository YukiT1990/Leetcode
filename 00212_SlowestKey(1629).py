# 1629. Slowest Key

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        durations = [releaseTimes[0]]
        longest_time = releaseTimes[0]
        index = 0
        for i in range(1, len(releaseTimes)):
            time = releaseTimes[i] - releaseTimes[i-1]
            durations.append(time)
            if longest_time <= time:
                longest_time = time
                index = i
        result = keysPressed[index]
        for i in range(len(durations)):
            if durations[i] == longest_time:
                if keysPressed[i] > result:
                    result = keysPressed[i]
        return result
        