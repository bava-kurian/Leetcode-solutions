#recursive solution to target sum problem
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        @lru_cache(maxsize=None)
        def helper(index,sum):
            if index==n:
                return 0 if sum!=target else 1
            return helper(index+1,sum+nums[index]) +helper(index+1,sum-nums[index])
        return helper(0,0)