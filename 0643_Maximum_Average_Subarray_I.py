class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        1. Calculate initial sum from 0 to k and store it in current sum and maximum sum
        2. Iterate through k to len(nums)
            1. Update current by adding new element in the window and substracting the first element of the window (with the distance=k)
            2. Update maximum sum
        3. Return maximum average
        """
        current = maximum = sum(nums[:k])
        for i in range(k, len(nums)):
            current += (nums[i] - nums[i - k])
            maximum = max(maximum, current)
        return maximum / k