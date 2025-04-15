class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        wind = 0
        re = float('inf')

        for r in range(len(nums)):
            wind += nums[r]

            while wind >= target:
                re = min(re, r - l + 1)
                wind -= nums[l]
                l += 1

        return 0 if re == float('inf') else re
