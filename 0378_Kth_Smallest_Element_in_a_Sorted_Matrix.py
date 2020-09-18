import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        General idea: use heap with element and it's coordinates
        1. Initialize heap as empty list and res = 0
        2. Use while loop for k > 0
            1. Pop from heap a tuple: current element, i, j - coordinates
            2. If it's first row -> push next in this row element to heap
            3. If it's not last row -> push next in this column to heap
            4. Decrease k
        3. Return res
        Attention: with first if i == 0 -> all possible columns coordinates will be added to the heap, there will be no need in this if when i > 0. All possible j will be popped from heap and for them -> only push elements from next rows with (i+1, j)
        """
        heap, res = [], 0
        heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            res, i, j = heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heappush(heap, (matrix[i][j+1], i, j+1))
            if i + 1 < len(matrix):
                heappush(heap, (matrix[i+1][j], i+1, j))
            k -= 1    
        return res