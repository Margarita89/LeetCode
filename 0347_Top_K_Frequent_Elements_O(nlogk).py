from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        General idea: use Counter to calculate all frequencies; use heap to push key, value pairs from counter keeping the size of heap <= k + 1 -> then it will be only log(k) to push and pop.
        """
        count_elements = Counter(nums)
        elem_freq = []
        i = 0
        for key, value in count_elements.items():
            heappush(elem_freq, (value, key))
            if i >= k: 
                heappop(elem_freq)
            i += 1
        return [key for _, key in elem_freq]