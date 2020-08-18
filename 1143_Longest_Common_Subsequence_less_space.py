class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        General idea: use 1D dynamic programming. Create dp of 0's, size min(n, m), where n, m are length of texts.
        1. Initialize dp with 0’s of the size min(n, m)
        2. Use prev_row and prev_diag to store values from the previous row and previous diagonal - it allows to reduce dp size from (n * m) to min(n, m)
        3. 2 nested loops to iterate through text1 and text2
            - If letters are equal –> update d[j] from previous cell without these letters (on diagonal) + 1
            - If not: max from previous (in row or in column)
        3. Return dp[-1]
        """
        m, n = map(len, (text1, text2))
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
        
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            prev_row, prev_diag = 0, 0
            for j in range(1, n + 1):
                prev_row, prev_diag = dp[j], prev_row
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + prev_diag #dp[i-1][j-1]
                else:
                    dp[j] = max(dp[j-1], prev_row) #dp[i][j-1]
        return dp[-1]