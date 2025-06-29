from collections import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if sum(nums) %2!=0: return False
        target=sum(nums)//2
        def helper(i,curr_summ):
            if target==curr_summ:
                return True
            if i>=n or curr_summ>target: 
                return False
            return helper(i+1,curr_summ+nums[i]) or helper(i+1,curr_summ)
        return helper(0,0)
            


 # Using memoization to check if we can partition the array into two subsets with equal sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        if sum(nums) %2!=0: return False
        target=sum(nums)//2
        @lru_cache(None)
        def helper(i,curr_summ):
            if target==curr_summ:
                return True
            if i>=n or curr_summ>target: 
                return False
            return helper(i+1,curr_summ+nums[i]) or helper(i+1,curr_summ)
        return helper(0,0)
    
    
    #usinsg tabulation to check if we can partition the array into two subsets with equal sum
    class Solution:
        def canPartition(self, nums: List[int]) -> bool:
            n=len(nums)
            if sum(nums) %2!=0: return False
            target=sum(nums)//2
            dp=[[False]*(target+1) for _ in range(n+1)]
            for i in range(n + 1):
                dp[i][0] = True

            for i in range(1, n + 1):
                for s in range(1, target + 1):
                    if s >= nums[i - 1]:
                        dp[i][s] = dp[i - 1][s] or dp[i - 1][s - nums[i - 1]]
                    else:
                        dp[i][s] = dp[i - 1][s]

            return dp[n][target]
                