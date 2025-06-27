#recursive solution to knapsack problem
# Given weights and values of n items, put these items in a knapsack of capacity W  
class Solution:
    def knapsack(self, W, val, wt):
        n=len(val)
        def helper(index,remain):
            if index>n-1 or remain==0:
                return 0
            exclude=helper(index+1,remain)
            include=0
            if remain>=wt[index]:
                include=val[index]+helper(index+1,remain-wt[index])
            return max(exclude,include)
        return helper(0,W)

#Memoization solution to knapsack problem
class Solution:
    def knapsack(self, W, val, wt):
        n=len(val)
        memo={}
        def helper(index,remain):
            if index>n-1 or remain==0:
                return 0
            if(index,remain) in memo:
                return memo[(index,remain)]
            exclude=helper(index+1,remain)
            include=0
            if remain>=wt[index]:
                include=val[index]+helper(index+1,remain-wt[index])
            memo[(index,remain)]=max(exclude,include)
            return memo[index,remain]
        return helper(0,W)

#top-down dynamic programming solution to knapsack problem

class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        memo = [[-1] * (W + 1) for _ in range(n + 1)]  # DP table

        def helper(index, remain):
            # Base cases
            if index == n or remain == 0:
                return 0

            # Return memoized result
            if memo[index][remain] != -1:
                return memo[index][remain]

            # Don't take current item
            exclude = helper(index + 1, remain)

            # Take current item if it fits
            include = 0
            if wt[index] <= remain:
                include = val[index] + helper(index + 1, remain - wt[index])

            # Save the result
            memo[index][remain] = max(include, exclude)
            return memo[index][remain]

        return helper(0, W)

