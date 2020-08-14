class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        General idea: dynamic programming, dp[i][j] - number of ways to roll dice i times with a sum of j.
        1. Initiate dp with 0's and additional row and column, dp[0][0] = 1 as there is only 1 way to get 0 with 0 dices (it's important in later steps)
        2. Iterate through dp (2 nested loops)
        3. Inside use 1 more loop to update dp[i][j] as a sum of all possible ways to get j as a sum from i-1 dice rolls:
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + .. dp[i-1][j-f]
        """
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        p = 10 **9 + 7
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1, min(j, f) + 1):
                    dp[i][j] += dp[i-1][j-k] 
                    dp[i][j] %= p
        return dp[-1][-1] % p