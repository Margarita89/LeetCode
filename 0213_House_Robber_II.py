class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        General idea: use dynamic programming and check 2 times - either without first house or without last. dp[i] stores maximum amount of money you can rob until ith house. 
        1. Base cases: nums is empty or the size is less than 4
        2. Method helper to find maximum amount of money that can be robbed until last house:
            1. Initialize dp as all zeros.
            2. dp[0] is nums[0] as it's max possible
            3. dp[1] is max from nums[0] and nums[1] - max possible
            4. Iterate through other houses and update dp as max between previous (which means current house is not robbed) and the one before previous + robbing current: dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            5. Return dp[-1]
        3. Call helper 2 times - either without first house or without last
        4. Return max from these calls
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)
        
        def helper(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0:2])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[-1]
        
        n1 = helper(nums[1:])
        n2 = helper(nums[:-1])
        return max(n1, n2)
        