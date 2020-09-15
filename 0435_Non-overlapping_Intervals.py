class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        General idea: intervals that have earlier ends will likely to be non-overlapping
        1. Sort intervals by ends
        2. Initialize counter and cur_end as minimum
        3. Iterate through intervals
            1. If start is less than cur_end there is overlapping -> increase counter
            2. Else -> update cur_end as end (this interval is not removed)
        4. Return counter
        """
        intervals.sort(key=lambda x: x[1])
        cur_end = float('-inf')
        counter = 0
        for start, end in intervals:
            if start < cur_end:
                counter += 1
            else:
                cur_end = end
        return counter