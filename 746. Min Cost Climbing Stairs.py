#memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        def helper(i):
            if i>=len(cost):
                return 0
            if i in memo:
                return memo[i]
            memo[i]= cost[i]+min(helper(i+1),helper(i+2))
            return memo[i]
        return min(helper(0),helper(1))
    
#tabular /bottom-up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])
        