class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for n in nums:
            s.append(n**2)
        return sorted(s)
    
    
    ### another solution
    # class Solution:
    # def sortedSquares(self, nums: List[int]) -> List[int]:
    #     s=[]
    #     m=0
    #     if nums[0] >= 0: # all positive
    #         s=[x**2 for x in nums]
    #         return s
    #     if len(nums)==1: # single number
    #         return [nums[0]**2]
    #     for i,n in enumerate(nums): #find +ve negative boundary
    #         if n>=0:
    #             m=i
    #             break
    #     if m==0: # all negative
    #         return  [x**2 for x in nums] [::-1]

    #     a=[x**2 for x in nums[m::]]
    #     b=[x**2 for x in nums[m-1::-1]]

    #     while(a and b): # merge
    #         if a[0]<=b[0]:
    #             s.append(a.pop(0))
                
    #         else :
    #             s.append(b.pop(0))
    #     if a :
    #         s+=[x for x in a]
    #     if b :
    #         s+=[x for x in b]
    #     return s

