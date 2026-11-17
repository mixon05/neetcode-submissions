from dataclasses import dataclass, astuple

@dataclass
class Interval:
    startTime: int
    endTime: int


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        new_interval = Interval(startTime, endTime)
        if len(self.events) == 0:
            self.events.append(new_interval)
            return True
        if endTime <= self.events[0].startTime:
            self.events.insert(0, new_interval)
            return True
        elif startTime >= self.events[-1].endTime:
            self.events.append(new_interval)
            return True
        for i in range(len(self.events) - 1):
            curr_end = self.events[i].endTime
            next_start = self.events[i + 1].startTime
            if startTime >= curr_end and endTime <= next_start:
                self.events.insert(i + 1, new_interval)
                return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)