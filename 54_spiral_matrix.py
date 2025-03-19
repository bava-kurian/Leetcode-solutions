class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        t=[]
        while(matrix):
            if matrix and matrix[0]:
                r+=(matrix.pop(0)) #first row
            if matrix and matrix[0]:
                for row in matrix:#last elemt of rest of the row
                    r.append(row.pop())
            if matrix and matrix[0]:
                t=matrix.pop() # last row in reverse 
                r+=t[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    r.append(row.pop(0))
        return r