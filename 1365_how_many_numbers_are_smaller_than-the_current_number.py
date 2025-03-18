class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        d={}
        for i,n in enumerate(s):
            if n not in d:
                d[n]=i
        r=[]
        for i in nums:
            r.append(d[i])
        return r