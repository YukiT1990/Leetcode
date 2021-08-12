# 1041. Robot Bounded In Circle

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
         # North (0, 1), West (-1, 0), South (0, -1), East (1, 0)
        direction = (0, 1)
        start_pos = [0, 0]

        for i in instructions:
            if i == 'G':
                start_pos[0] += direction[0]
                start_pos[1] += direction[1]
            elif i == 'L':
                direction = (-direction[1], direction[0])
                # North (0, 1) -> West (-1, 0) -> South (0, -1) -> East (1, 0)
            elif i == 'R':
                direction = (direction[1], -direction[0])
                # North (0, 1) -> East (1, 0) -> South (0, -1) -> West (-1, 0)

        return start_pos == [0, 0] or direction != (0, 1)
        # if start_pos != [0, 0] and direction != (0, 1), it will
        # return to the original state(start_pos = [0, 0]
        # and direction = (0, 1)) after four times of iteration.
