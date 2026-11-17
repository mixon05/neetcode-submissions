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
        if len(self.events) == 0:
            self.events.append(new_interval)
            return True
        if idx == 0:
            if endTime <= self.events[idx].startTime:
                self.events.insert(idx, new_interval)
                return True
            return False
        if idx == len(self.events):
            if startTime >= self.events[-1].endTime:
                self.events.append(new_interval)
                return True
            return False
        prev_end = self.events[idx - 1].endTime
        curr_start = self.events[idx].startTime
        if startTime >= prev_end and endTime <= curr_start:
            self.events.insert(idx, new_interval)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)