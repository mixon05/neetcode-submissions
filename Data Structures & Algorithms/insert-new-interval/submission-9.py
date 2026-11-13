class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda t: t[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = res[-1][0], res[-1][1]
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if prev_end >= curr_start:
                res[-1][1] = max(prev_end, curr_end)
            else:
                res.append(intervals[i])
        return res