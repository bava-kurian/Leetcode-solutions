class Solution:
    
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + helper(i+2), helper(i+1))
        
        return helper(0)

