from collections import Counter

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        counter = Counter(nums)    
        l = list(counter.keys()) 
        nums[:len(l)] = l 
        
        return len(l)
