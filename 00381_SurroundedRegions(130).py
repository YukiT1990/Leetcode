# 130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # edge cases
        if not board:
            return
        if len(board[0]) == 1 or len(board) == 1:
            return
        
        def dfs(x, y):
            if board[y][x] == "O":
                board[y][x] = "a"
                if x < len(board[0]) - 1:
                    dfs(x+1, y)
                if x > 0:
                    dfs(x-1, y)
                if y < len(board) - 1:
                    dfs(x, y+1)
                if y > 0:
                    dfs(x, y-1)
                    
        #dfs all border "O"s and make them into any random letter (using "a" in the dfs function)
        for index, value in enumerate(board):
            dfs(0, index)
            dfs(len(board[0]) - 1, index)
        for index, value in enumerate(board[0]):
            dfs(index, 0)
            dfs(index, len(board) - 1)
            
        #go through the entire board changing "a"s to "O" and all remaining "O"s to "X"
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "a":
                    board[y][x] = "O"
                elif board[y][x] == "O":
                    board[y][x] = "X"