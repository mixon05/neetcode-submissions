class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            if newInterval[0] > end:
                res.append([start, end])
            elif newInterval[1] < start:
                return res + [newInterval] + intervals[i:]
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        return res + [newInterval]
