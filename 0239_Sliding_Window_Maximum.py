from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        General idea: use deque with indexes such that they represent elements in descending order
        1. Iterate through elements in nums
        2. Keep deque such that new element is no less than last indexed from deque
        3. Append new index to deque
        4. If the size of window is larger than k -> popleft first element
        5. Starting from i > k-1 -> append first indexed element from deque to answer
           First k-1 just add elements to deque preparing them for window
        """
        output = []
        q = deque()
        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(i)
            if q[0] == i - k:
                q.popleft()
            if i >= k-1:
                output.append(nums[q[0]])
        return output
            
            