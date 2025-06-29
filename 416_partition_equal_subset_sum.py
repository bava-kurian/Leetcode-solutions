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
            


            