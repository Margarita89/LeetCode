class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        General idea: dynamic programming. dp[i] is number of combinations to make amount i.
        1. Initialize dp with first 1 and others zeros, dp[0] = 1 as 1 combination of 0 coins is needed to make amount 0
        2. Iterate through coins
            1. Iterate from coin till (amount + 1) to update dp
            2. Update dp[i] by adding dp[i-coin], which is the number of combinations to make (i - coin). By adding a coin we will get dp[i] from dp[i-coin]
        3. Return dp[-1]

        """
        dp = [1] + [0] * amount    
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]
        