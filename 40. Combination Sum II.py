from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, s = [], []

        def backtrack(start):
            if sum(s) == target:
                ans.append(s[:])
                return
            if sum(s) > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                # skip duplicates at the same level
                if candidates[i] == prev:
                    continue
                s.append(candidates[i])
                backtrack(i + 1)   # move forward
                s.pop()
                prev = candidates[i]

        backtrack(0)
        return ans
