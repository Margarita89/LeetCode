class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        General idea: dynamic programming. dp[i] is min coins to make amount i
        1. Initialize dp with 'inf' and size (amount + 1), dp[0] = 0 as 0 coins is needed to make amount 0
        2. Iterate through coins
            1. Iterate from coin till (amount + 1) to update dp
            2. update dp[i] as min from dp[i] and dp[i-coin] + 1, which is the amount of coins needed to make (i-coin) + 1 coin
        3. Return dp[-1] if it was updates, otherwise -1
        """
        dp = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1) 
        return dp[-1] if dp[-1] != float('inf') else -1
                