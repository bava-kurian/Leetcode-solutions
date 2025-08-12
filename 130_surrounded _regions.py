class Solution:
    def solve(self, board):
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'S'  # mark as safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            dfs(r, 0)         # left border
            dfs(r, cols-1)    # right border
        for c in range(cols):
            dfs(0, c)         # top border
            dfs(rows-1, c)    # bottom border
        
        # Step 2: Flip and restore
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
