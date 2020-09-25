from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        General idea: use Counter to calculate all frequencies; use heap to push key, value pairs from counter keeping the size of heap <= k + 1 -> then it will be only log(k) to push and pop.
        """
        count_elements = Counter(nums)
        elem_freq = []
        for key, value in count_elements.items():
            heappush(elem_freq, (value, key))
            if len(elem_freq) > k: 
                heappop(elem_freq)
        return [key for _, key in elem_freq]