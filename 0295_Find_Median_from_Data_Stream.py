import heapq
class MedianFinder:
    """
    General idea: use 2 heaps, equally separating data into min half (max_heap) and max half (min_heap)
    1. Method addNum:
        1. Add num into min_heap and also extract the min number
        2. Push this number into max_heap (using '-' to make max_heap real max heap) and pop the max number
        3. Push to min_heap or to max_heap to keep sizes equal (or different by 1), prefering min_heap
    2. Method findMedian:
        1. If min_heap is larger -> return min from min_heap
        2. Else: median from min_heap and max_heap
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        
    def addNum(self, num: int) -> None:
        num = heappushpop(self.min_heap, num)
        num = -heappushpop(self.max_heap, -num)
        if len(self.min_heap) <= len(self.max_heap):
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()