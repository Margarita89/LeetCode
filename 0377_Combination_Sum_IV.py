class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        General idea: use dynamic programming. dp[i] - number of possible combinations to sum to i.
        1. Initialize dp with all zeros, except first element 1 as there is 1 combination to sum to 0.
        2. Iterate through dp
            1. Iterate through numbers
                1. If current sum is no less than current num -> Update dp[i] by adding dp[i-num], which is the number of combinations to make (i - num). By adding a num we will get dp[i] from dp[i-num]
        3. Return dp[-1]
        """
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        return dp[-1]
    
