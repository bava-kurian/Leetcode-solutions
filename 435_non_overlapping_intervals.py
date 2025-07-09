from cmath import inf


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print(intervals)
        end=float(-inf)
        c=0
        for i in range(len(intervals)):
            start,finish=intervals[i]
            if start>=end:
                end=finish
            else:
                c+=1
        return c
        