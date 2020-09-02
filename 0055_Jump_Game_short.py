class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        General idea: start from the end and check if it's possible to get to the beginning using a pointer that keeps track on the last position that it possible to reach. Can be done from start to end also.
        1. Initialize last_pos pointer to point to the last index
        2. Iterate from end to start
            1. If the it's possible to get to last_pos from current index -> update last_pos to current index
        3. Return True if last_pos is 0, else: False
        """
        last_pos = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0
        