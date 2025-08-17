from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            # if we've used all chars → valid partition
            if start == len(s):
                res.append(path[:])
                return

            # try all possible cuts
            for i in range(start, len(s)):
                substr = s[start:i+1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(i+1, path)
                    path.pop()

        backtrack(0, [])
        return res
