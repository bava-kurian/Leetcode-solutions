class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        def helper(start,curr):
            if len(curr)==k:
                result.append(curr[:])
                return 
            for j in range(start,n+1):
                curr.append(j)
                helper(j+1,curr)
                curr.pop()
        helper(1,[])
        return result

        
