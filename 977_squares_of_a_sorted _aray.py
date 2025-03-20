class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for n in nums:
            s.append(n**2)
        return sorted(s)