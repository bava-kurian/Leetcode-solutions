class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def helper (nums,i,subset):
            if i == len(nums):
                output.append(subset.copy())
                return
            helper(nums,i+1,subset)
            subset.append(nums[i])
            helper(nums,i+1,subset)
            subset.pop()
        helper(nums,0,[])
        return output
    
    # memoization

    def fib(self, n: int) -> int:
        hash={}
        def f(n):
            if n in hash:
                return hash[n]
            if n<=1:
                return n
            hash[n]=self.fib(n-1)+self.fib(n-2)
            return hash[n]
        return f(n)
    
    
#Tabulation

