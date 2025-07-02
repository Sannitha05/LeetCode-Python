class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        self.backtracking(0,board,ans,n)
        return ans

    def backtracking(self, r: int, board: List[str], ans: List[List[str]], n: int):
        if r == n:
            ans.append(board[:])
            return
        for c in range(n):
            if self.safe(r, c, board, n):
                row_list = list(board[r])
                row_list[c] = 'Q'
                board[r] = ''.join(row_list)
                self.backtracking(r + 1, board, ans, n)
                row_list[c] = '.'
                board[r] = ''.join(row_list)
    
    def safe(self, r: int, c: int, board: List[str], n: int) -> bool:
        for i in range(r):
            if board[i][c] == 'Q':
                return False
        i, j = r, c
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = r, c
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True
