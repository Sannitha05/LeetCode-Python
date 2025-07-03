class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col:
                    return False
            
            for i in range(row):
                if board[i] - i == col - row:
                    return False
            
            for i in range(row):
                if board[i] + i == col + row:
                    return False
            
            return True
        
        def backtrack(board, row):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    count += backtrack(board, row + 1)
            
            return count
        
        board = [-1] * n
        return backtrack(board, 0)