class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        @lru_cache(None)
        def helper(i,j):
            if i>=m or j>=n:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            return helper(i+1,j)+helper(i,j+1)
        return helper(0,0)
            