from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        i = 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1

        if i == len(nums):
            return True  # all elements are equal

        if nums[i] > nums[i - 1]:
            # Increasing
            for j in range(i, len(nums)):
                if nums[j] < nums[j - 1]:
                    return False
        else:
            # Decreasing
            for j in range(i, len(nums)):
                if nums[j] > nums[j - 1]:
                    return False

        return True
