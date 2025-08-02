from collections import Counter
class Solution:
    '''def findDuplicate(self, nums: List[int]) -> int:
        c=dict(Counter(nums))
        for i in c.keys():
            if c[i]>=2:
                return i
        return None'''
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1