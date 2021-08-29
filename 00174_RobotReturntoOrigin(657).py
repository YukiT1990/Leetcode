# 657. Robot Return to Origin

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 72 ms	14.5 MB
        # original_position = [0, 0]
        # for char in moves:
        #     if char == 'R':
        #         original_position[0] += 1
        #     elif char == 'L':
        #         original_position[0] -= 1
        #     elif char == 'U':
        #         original_position[1] += 1
        #     elif char == 'D':
        #         original_position[1] -= 1
        # if original_position[0] == 0 and original_position[1] == 0:
        #     return True
        # else:
        #     return False
        

        # 52 ms	14.4 MB
        # left_right = 0
        # up_down = 0
        # for char in moves:
        #     if char == 'R':
        #         left_right += 1
        #     elif char == 'L':
        #         left_right -= 1
        #     elif char == 'U':
        #         up_down += 1
        #     elif char == 'D':
        #         up_down -= 1
        # if left_right == 0 and up_down == 0:
        #     return True
        # else:
        #     return False
        

        # 28 ms	14.1 MB
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')