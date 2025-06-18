class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]:
        l=len(nums)
        result=[]
        def helper(index):
            if index==l-1:
                result.append(nums[:])
                return 
            for j in range(index,l):
                nums[index],nums[j]=nums[j],nums[index]
                helper(index+1)
                nums[j],nums[index]=nums[index],nums[j]
        helper(0)
        return result
            
        