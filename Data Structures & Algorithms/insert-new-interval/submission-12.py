class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda t: t[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if prev_end >= start:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res