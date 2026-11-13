class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda t: t[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            prev_end = result[-1][1]
            if prev_end >= start:
                result[-1][1] = max(prev_end, end)
            else:
                result.append([start, end])
        return result