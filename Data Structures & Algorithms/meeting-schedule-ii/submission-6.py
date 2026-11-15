"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i: i.start)
        heap = [intervals[0].end]
        min_rooms = 1
        for interval in intervals[1:]:
            if heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            min_rooms = max(min_rooms, len(heap))
        # return min_rooms
        return len(heap)