# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_n = set(row)
            row_n.remove(".")
            # print(row_n)
            for n in row_n:
                if row.count(n) > 1:
                    return False
                    
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            column_n = set(column)
            column_n.remove(".")
            # print(column_n)
            for n in column_n:
                if column.count(n) > 1:
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = []
                sub_box += board[i + 0][j:j+3]
                sub_box += board[i + 1][j:j+3]
                sub_box += board[i + 2][j:j+3]
                sub_box_n = set(sub_box)
                sub_box_n.remove(".")
                # print(sub_box_n)
                for n in sub_box_n:
                    if sub_box.count(n) > 1:
                        return False
                
        return True
        