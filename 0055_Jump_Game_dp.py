class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        General idea: use dynamic programming. dp[i] is 1 if it's possible to get to ith index.
        1. Initialize dp with 0s, first element is 1, as we start from first.
        2. Iterate through array
            1. Iterate through already visited indexes
                1. If it's possible to get to already visited index (dp[j] == 1) and it's possible to get from it to current (j + nums[j] >= i) -> update dp[i] and break
        3. Return dp[-1] == 1
        """
        dp = [0] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in reversed(range(i)):
                if dp[j] == 1 and j + nums[j] >= i: # means it's enough to jump to ith index
                    dp[i] = 1
                    break
        return dp[-1] == 1