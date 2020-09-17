class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        General idea: memorize last occupied seat while traversing the list of seats. Use it to calculate max_distance
        1. Find first occupied seat and save it as start
        2. Initialize max_distance as start. If start is 0 - then max_distance = 0, if start is not 0, then max_distance - is the distance to it (the 0 index seat is chosen)
        3. Iterate from start + 1 until end of list of seats
            1. If seat is occupied -> update max_distance and start as current seat
        4. If last seat was not occupied -> update max_distance
        5. Return max_distance
        """
        i = 0
        while seats[i] != 1:
            i += 1
        start = i
        max_distance = start
        for i in range(start + 1, len(seats)):
            if seats[i] == 1:
                max_distance = max(max_distance, (i - start) // 2)
                start = i
        if seats[-1] == 0:
            max_distance = max(max_distance, (i - start))
        return max_distance