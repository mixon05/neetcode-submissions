"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda t: t.start)
        prev_end = 0
        for interval in intervals:
            start, end = interval.start, interval.end
            if prev_end > start:
                return False
            prev_end = end
        return True