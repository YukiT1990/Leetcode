# 1275. Find Winner on a Tic Tac Toe Game

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['-' for _ in range(3)] for _ in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                board[moves[i][0]][moves[i][1]] = 'X'
            else:
                board[moves[i][0]][moves[i][1]] = 'O'
        
                
        if (board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
            return 'A'
        elif (board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
            return 'B'
        elif board[0].count('-') == 0 and board[1].count('-') == 0 and board[2].count('-') == 0:
            return "Draw"
        else:
            return "Pending"