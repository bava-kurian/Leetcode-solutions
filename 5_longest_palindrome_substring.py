#itrative solution to find the longest palindromic substring
# Time complexity: O(n^3)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        max_p = s[0]
        
        def is_palindrome(sub):
            return sub == sub[::-1]
        
        for i in range(n):
            for j in range(i+1, n):
                current = s[i:j+1]
                if is_palindrome(current) and len(current) > len(max_p):
                    max_p = current
        
        return max_p
    
    
