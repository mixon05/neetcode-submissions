class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda t: t[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:
            prev_end = result[-1][1]
            curr_start, curr_end = start, end
            if prev_end >= curr_start:
                result[-1][1] = max(prev_end, curr_end)
            else:
                result.append([start, end])
        return result