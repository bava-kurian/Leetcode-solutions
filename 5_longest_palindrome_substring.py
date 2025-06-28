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
    
    
#dynamic programming solution to find the longest palindromic substring
# Time complexity: O(n^2)   
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        for i in range(n):
            dp[i][i] = True  # Single character

        for end in range(1, n):
            for start_idx in range(end):
                if s[start_idx] == s[end]:
                    if end - start_idx == 1 or dp[start_idx + 1][end - 1]:
                        dp[start_idx][end] = True
                        if end - start_idx + 1 > max_len:
                            max_len = end - start_idx + 1
                            start = start_idx

        return s[start:start + max_len]
