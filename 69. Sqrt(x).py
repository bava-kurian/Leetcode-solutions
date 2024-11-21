class Solution:
    def mySqrt(self, x: int) -> int:
        u=x
        l=0
        r=0
        while l<=u:
            m=(l+u)//2
            if m**2>x:
                u=m-1
            elif m**2<x:
                l=m+1
                r=m
            else:
                return m;
        return r;
            