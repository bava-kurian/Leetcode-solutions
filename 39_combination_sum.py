from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def helper(start, curr, total):
            if total == target:
                result.append(curr[:])
                return
            if total > target:
                return
            
            for j in range(start, n):
                curr.append(candidates[j])
                helper(j, curr, total + candidates[j])  # j instead of j+1 → allows reuse
                curr.pop()

        helper(0, [], 0)
        return result
