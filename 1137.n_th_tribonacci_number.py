#memoization
class Solution:
    def tribonacci(self, n: int) -> int:
        memo={}
        def helper(index):
            if index==0:
                return 0
            elif index==1 or index==2:
                return 1
            if index not in memo:
                memo[index]=helper(index-3)+helper(index-2)+helper(index-1)
            return memo[index]
        return helper(n)
