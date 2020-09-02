class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        General idea: convert hours into minutes and choose between 2 options: hours are larger than minutes or visa versa. 
        1. Convert hour in 60 minutes
        2. Calculate 2 angles and choose min
        12h -> 0
        1h -> 1
        ..
        10 min -> 5 * 10/60
        15 min -> 5 * 15/60
        30 min -> 5 * 30/60
        """
        hour_in_min = hour % 12 *5.0 + 1/12 * minutes #float
        print(hour_in_min)
        angle1, angle2 = float('inf'), float('inf')
        if hour_in_min >= minutes:
            angle1 = min(hour_in_min - minutes, 60 - hour_in_min + minutes) * 6
        else:
            angle2 = min(minutes - hour_in_min, 60 - minutes + hour_in_min) * 6
        return (min(angle1, angle2))