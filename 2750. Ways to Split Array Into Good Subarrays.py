class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        ones = [i for i, v in enumerate(nums) if v == 1]
        if not ones:
            return 0  # no 1s → impossible to split
        
        ans = 1
        for i in range(1, len(ones)):
            gap = ones[i] - ones[i-1] - 1
            ans = (ans * (gap + 1)) % MOD
        
        return ans
