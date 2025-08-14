#recursive solution
class Solution:
    
    def countSubstrings(self, s: str) -> int:
        def is_pal(s,left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        n=len(s)
        def helper(start,end):
            if start>end:
                return 0
            count=0
            if is_pal(s,start,end):
                count+=1
            
            count += helper(start + 1, end)
            count += helper(start, end - 1)
            count -= helper(start + 1, end - 1)
            
            return count

        return helper(0, n - 1)
            
        