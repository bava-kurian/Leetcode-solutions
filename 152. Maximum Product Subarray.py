#recursive sol
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def helper(i):
            
            if i == 0:
                return nums[0], nums[0], nums[0]

            prev_max, prev_min, prev_global = helper(i - 1)

            max_here = max(nums[i], nums[i] * prev_max, nums[i] * prev_min)
            min_here = min(nums[i], nums[i] * prev_max, nums[i] * prev_min)

            global_max = max(prev_global, max_here)

            return max_here, min_here, global_max

        return helper(len(nums) - 1)[2]
