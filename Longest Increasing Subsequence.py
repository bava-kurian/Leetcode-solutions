class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            
            idx = bisect.bisect_left(sub, x)
            if idx == len(sub):
                sub.append(x) 
            else:
                sub[idx] = x  
        return len(sub)
    
    class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)