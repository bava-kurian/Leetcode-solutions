class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        found=False
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == target:
                    found=True
        return found