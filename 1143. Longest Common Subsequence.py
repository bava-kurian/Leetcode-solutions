
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