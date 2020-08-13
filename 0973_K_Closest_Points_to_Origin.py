import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        General idea: use min heap.
        1. Iterate through all points
        2. Push to heap (-square, point) to be able to pop extra from top 
        (when the size of the heap is K+1)
        3. Return points from heap
        """
        heap = [] 
        for point in points:
            square = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (-square, point))
            if len(heap) == K + 1:
                _ = heapq.heappop(heap)       

        return [point for _, point in heap]