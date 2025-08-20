class Solution:
    def integerBreak(self, n: int) -> int:
        @lru_cache(None)
        def helper(i):
            if i == 2: return 1
            if i == 3: return 2
            r=0
            for j in range(1,i):
                r=max(r,max(j*(i-j),j*helper(i-j)))
            return r
        return helper(n)