import bisect
class MyCalendar(object):
    """
    General idea: use bisect to check if interval can be inserted
    1. Get index using bisect_left - where interval could be inserted (the left possible)
    2. Initialize 2 bool variables to check if all intervals on the left don't intersect with start and to check if all intervals on the right don't intersect with end of our interval
    3. If both conditions are true -> insert interval and return True
    4. Else: -> return False
    """

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect.bisect_left(self.intervals, [start, end])
        is_left = idx == 0 or self.intervals[idx-1][1] <= start
        is_right = idx == len(self.intervals) or self.intervals[idx][0] >= end
        if is_left and is_right:
            self.intervals.insert(idx, [start, end])
            return True
        return False
            
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)