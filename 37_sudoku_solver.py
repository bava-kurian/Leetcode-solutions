class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {(i, j): set() for i in range(3) for j in range(3)}
        empty_cells = []

        # Step 1: Fill initial sets and collect empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3, c//3)].add(num)

        # Step 2: Backtracking function
        def backtrack(index):
            if index == len(empty_cells):
                return True  # solved
            r, c = empty_cells[index]
            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[(r//3, c//3)]:
                    # Place number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3, c//3)].add(num)

                    if backtrack(index + 1):
                        return True  # valid path

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[(r//3, c//3)].remove(num)
            return False

        backtrack(0)
