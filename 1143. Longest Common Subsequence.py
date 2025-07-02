
#recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        def helper(i,j):
            if i>(n-1) or j>(m-1):
                return 0
            if text1[i]==text2[j]:
                return 1+helper(i+1,j+1)
            return max(helper(i+1,j),helper(i,j+1))
        return helper(0,0)
    
#memoization
from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        @lru_cache(None)
        def helper(i,j):
            if i>(n-1) or j>(m-1):
                return 0
            if text1[i]==text2[j]:
                return 1+helper(i+1,j+1)
            return max(helper(i+1,j),helper(i,j+1))
        return helper(0,0)
#tabulation

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # Create a (n+1) x (m+1) DP table initialized to 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Fill the table from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # The answer is in dp[0][0]
        return dp[0][0]
