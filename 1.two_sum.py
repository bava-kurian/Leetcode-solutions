class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            if target-nums[i] in hash:
                return [i,hash[target-nums[i]]]
            else:
                hash[nums[i]]=i
        return []