class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        no=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                no.append(i)
                
        return no