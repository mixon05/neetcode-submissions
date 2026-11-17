from dataclasses import dataclass, astuple
from bisect import bisect_left

@dataclass(order=True)
class Interval:
    startTime: int
    endTime: int


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        new_interval = Interval(startTime, endTime)
        idx = bisect_left(self.events, new_interval)

        if idx > 0 and startTime < self.events[idx - 1].endTime:
            return False
        elif idx < len(self.events) and endTime > self.events[idx].startTime:
            return False
        self.events.insert(idx, new_interval)
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)