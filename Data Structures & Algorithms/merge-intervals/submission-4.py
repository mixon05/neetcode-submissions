class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda t: t[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev_start, prev_end = result[-1][0], result[-1][1]
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if prev_end >= curr_start:
                result[-1][1] = max(prev_end, curr_end)
            else:
                result.append(intervals[i])
        return result