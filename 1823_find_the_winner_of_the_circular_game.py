class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1, n + 1))  # Players numbered from 1 to n
        idx = 0
        while len(l) > 1:
            idx = (idx + k - 1) % len(l)
            l.pop(idx)
        return l[0]
