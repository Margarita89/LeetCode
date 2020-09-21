class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        """
        General idea: use dynamic programming. dp[i][j] - if it's possible to sum up to i using first j elements
        1. Check if sum of all elements in nums is even. If not -> return False
        2. Initialize empty dp array with additional row and column with all Falls
        3. Let the first row be True -> if it's possible to sum up to 0. Yes, it's possible, just don't use elements 
        4. Use 2 nested loops to fill dp starting from 1st indexes
            1. If current i is smaller than the number in nums -> number could not be used for the sum to i -> dp[i][j] = dp[i][j-1] (if with previous numbers the sum was done, adding current number wouldn't change it)
            2. Else: either without current number (dp[i][j-1]) or with current number, but check first that the sum = i - current number was obtained (dp[i - nums[j-1]][j-1])
        5. Return dp[-1][-1]
        """
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [[False for _ in range(len(nums) + 1)] for _ in range(target + 1)]
        for i in range(len(dp[0])):
            dp[0][i] = True
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if i < nums[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] or dp[i - nums[j-1]][j-1]
        return dp[-1][-1]
        