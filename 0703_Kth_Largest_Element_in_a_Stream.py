#from heapq import heappushpop
class KthLargest:
    """
    General idea: use heap
    1. Iterate through nums and push num to heap. 
        1. If index is larger or equal to k -> also pop from heap. It's possible to use heapify
    2. If size of heap is less than k -> just push val
    3. Else -> use heappushpop (push val and pop from heap to keep it size k)
    4. Return top element from heap
    """
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for i, num in enumerate(nums):
            heappush(self.heap, num)
            if i >= k:
                heappop(self.heap)
        #print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]
    
    



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)