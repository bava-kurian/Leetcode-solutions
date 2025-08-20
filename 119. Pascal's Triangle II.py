class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for r in range(rowIndex+1):
            row = [1] * (r + 1) 
            for c in range(1, r):
                row[c] = triangle[r-1][c-1] + triangle[r-1][c]
            triangle.append(row)

        return triangle[rowIndex]

        