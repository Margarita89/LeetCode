class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        General idea: use 2 pointers starting from beginning of each interval and move them forward
        1. Initialize 2 starting pointers for A and B and answering list 'intersect'
        2. Use while loop to iterate through intervals A and B
            1. Create bool variables to check if current start of interval from A intersects with current interval from B and the same for the current start of interval from B
            2. If any of this is True -> there is intersection
                1. Start is max from starts of current in intervals from A and B
                2. End is min from ends of current in intervals from A and B
                3. Append [start, end] interval to intersect
            3. If end of A is before end of B -> move pointer for the next interval from A
            4. Else -> move pointer for the next interval from B
        3. Return intersect
        """
        intersect = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            a_intersect_b = B[j][0] <= A[i][0] <= B[j][1]
            b_intersect_a = A[i][0] <= B[j][0] <= A[i][1] 
            if a_intersect_b or b_intersect_a:
                start = max(A[i][0], B[j][0])
                end = min(A[i][1], B[j][1])
                intersect.append([start, end])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return intersect