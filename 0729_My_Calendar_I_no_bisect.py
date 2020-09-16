class MyCalendar(object):
    """
    General idea: cycle through list of intervals to check if [start, end] could be inserted
    1. Iterate through list of intervals
        1. If [start, end] intersect with current interval -> return False
    2. Insert interval
    3. Return True
    Attention: list of intervals is not necesseraly sorted
    """

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.intervals:
            if s < end and start < e:
                return False
        self.intervals.append([start, end])
        return True
            
            


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)