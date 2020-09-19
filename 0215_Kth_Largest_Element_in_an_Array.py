class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        General idea: use heap
        1. Heapify nums
        2. Use while loop to decrease size of heap to k -> pop from heap. After this loop, the heap will be size of k
        3. Return top of the heap
        """
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        return nums[0]
        