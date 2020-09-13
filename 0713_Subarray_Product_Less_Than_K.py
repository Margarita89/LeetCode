class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        General idea: use sliding window with 2 pointers - to start and end of the window
        1. Initialize start pointer = 0
        2. Initialize 'ans' - number of (contiguous) subarrays and product = 1
        3. Iterate through all nums
            1. Update product by multipling 
            2. Use while loop to move start pointer if product >= k
                1. Update product by dividing
                2. Increase start pointer
            3. Update ans (after while loop product is less than k). Attention: here it's important to add all subarrays that end at 'end'.
        4. Return ans
        """
        start = 0
        ans = 0
        product = 1
        for end in range(len(nums)):
            product *= nums[end]
            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            ans += end - start + 1
        return ans