class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, (start, end) in enumerate(intervals):
            if end < newInterval[0]:
                res.append([start, end])
            elif start > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        res.append(newInterval)
        return res