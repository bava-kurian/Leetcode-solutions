class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for r in range(numRows):
            row = [1] * (r + 1)   # row length = r+1
            for c in range(1, r):
                row[c] = triangle[r-1][c-1] + triangle[r-1][c]
            triangle.append(row)

        return triangle
