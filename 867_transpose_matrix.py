class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [list(row) for row in zip(*matrix)]
        return res