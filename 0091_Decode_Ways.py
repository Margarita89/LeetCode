class Solution:
    def numDecodings(self, s: str) -> int:
        """
        General idea: use dynamic programming. dp[i] is a total number of ways to decode until i.
        1. Initialize dp as 1 and all other zeros. It's always possible to decode 0-long message.
        2. If first number is not 0 -> dp[1] = 1
        3. Iterate through message starting from first index
            1. Initialize one as an int of 1 current digit. Two as an int of 2 digits (current and previous)
            2. If one is not zero -> update dp[i] += dp[i-1] as it will include all options to decode for (i-1)
            3. If two is between 10 and 26 -> update dp[i] += dp[i-2] as it will include all options to decode for (i-2) also
        4. Return dp[-1]
        """
        dp = [1] + [0] * len(s)
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            one = int(s[i-1:i])
            two = int(s[i-2:i])
            if one != 0:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[-1]