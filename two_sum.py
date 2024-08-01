class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i