from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, k):
            if k == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[k]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # mark visited

            found = (dfs(r+1, c, k+1) or
                     dfs(r-1, c, k+1) or
                     dfs(r, c+1, k+1) or
                     dfs(r, c-1, k+1))

            board[r][c] = temp  # restore
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
