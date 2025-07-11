class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        arrow=1
        end=points[0][1]
        for start,finish in points[1:]:
            if start>end:
                arrow+=1
                end=finish
        return arrow
        