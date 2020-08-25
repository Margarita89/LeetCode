class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        General idea: use 2 pointers (from start and end)
        1. Initialize empty container called "max_container" and pointers to first and last heights
        2. Use while loop with 2 pointers
            1. Update max_container as a max from previous and current
            2. If the height of left (p1) is lower than the height of right -> move left
            3. Else -> move right
        3. Return max_container
        """
        max_container = 0
        p1, p2 = 0, len(height)-1
        while p1 < p2:
            max_container = max(max_container, (p2-p1) * min(height[p1], height[p2]))
            if height[p1] < height[p2]:
                p1 += 1
            else:
                p2 -= 1
        return max_container