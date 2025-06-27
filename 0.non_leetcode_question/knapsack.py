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


