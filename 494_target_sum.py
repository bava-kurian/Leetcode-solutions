#recursive solution using memoization to find the number of ways to achieve a target sum with given numbers using lru_cache
from functools import lru_cache
from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @lru_cache(maxsize=None)
        def helper(index,sum):
            if index==n:
                return 0 if sum!=target else 1
            return helper(index+1,sum+nums[index]) +helper(index+1,sum-nums[index])
        return helper(0,0)
    
#susing memoization to find the number of ways to achieve a target sum with given numbers using dictionary
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def helper(index,sum):
            if index==n:
                return 0 if sum!=target else 1
            if (index,sum) not in memo:
                memo[(index,sum)]=helper(index+1,sum+nums[index]) +helper(index+1,sum-nums[index])
            return memo[index,sum]
        return helper(0,0)