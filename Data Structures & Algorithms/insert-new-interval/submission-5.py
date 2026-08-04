class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        found = False
        for i in range(len(intervals)):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                found = True
                break
        if not found:
            intervals.append(newInterval)

        result = [intervals[0]]
        for start, end in intervals[1:]:
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result