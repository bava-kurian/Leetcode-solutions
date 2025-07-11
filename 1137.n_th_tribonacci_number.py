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

#tabulation
class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        dp=[0]*(n+2)
        dp[0], dp[1], dp[2] = 0, 1, 1
        for i in range(3,n+1):
                dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        return dp[n]
            
#space optimization
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        return c
