# 999. Available Captures for Rook

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        result = 0
        R_pos = [-1, -1]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    R_pos[0] = i
                    R_pos[1] = j
                    break
                    
        for k in range(R_pos[0], -1, -1):
            if board[k][R_pos[1]] == 'B':
                break
            if board[k][R_pos[1]] == 'p':
                result += 1
                break
        for k in range(R_pos[0], len(board)):
            if board[k][R_pos[1]] == 'B':
                break
            if board[k][R_pos[1]] == 'p':
                result += 1
                break
        for k in range(R_pos[1], -1, -1):
            if board[R_pos[0]][k] == 'B':
                break
            if board[R_pos[0]][k] == 'p':
                result += 1
                break
        for k in range(R_pos[0], len(board[0])):
            if board[R_pos[0]][k] == 'B':
                break
            if board[R_pos[0]][k] == 'p':
                result += 1
                break
                
        return result