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
#tabular solution
def maxProduct(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod  # swap when negative

        max_prod = max(nums[i], nums[i] * max_prod)
        min_prod = min(nums[i], nums[i] * min_prod)

        result = max(result, max_prod)

    return result