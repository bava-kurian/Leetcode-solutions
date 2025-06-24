class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def helper(index):
            if index >= n:
                return 0
            if index in memo:
                return memo[index]

            one_step = cost[index] + helper(index + 1)
            two_step = cost[index] + helper(index + 2)
            memo[index] = min(one_step, two_step)

            return memo[index]

        return min(helper(0), helper(1))

# Tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = second = 0

        for i in range(n - 1, -1, -1):
            current = cost[i] + min(first, second)
            first, second = current, first

        return min(first, second)
