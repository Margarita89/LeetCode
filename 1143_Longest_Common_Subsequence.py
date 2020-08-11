class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        General idea: create 0's dp with the size (len(text1) + 1) * (len(text2) + 1).              Update values if there are equal letters or
           Dp[i][j] = max(dp[i-1][j], dp[i][j-1]) – max of previous ones
        1. Initialize dp with 0’s of the size (len(text1) + 1) * (len(text2) + 1)
        2. 2 nested loops to iterate through text1 and text2
            - If letters are equal –> update d[i][j] from previous cell without                       these letters (on diagonal) + 1
            - If not: max from previous (in row or in column)
        3. Return dp[-1][-1]

        """
        if len(text1) == 0 or len(text2) == 0:  
            return 0
        
        dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]