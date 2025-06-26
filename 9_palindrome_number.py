class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=m=str(x)
        n=n[::-1]
        print(n)
        if n==m:
            return True
        return False