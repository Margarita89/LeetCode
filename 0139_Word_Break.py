class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        General idea: use dynamic programming. dp[i] is whether it's possible to break string until ith character.
        1. Initialize dp with all False, except first element True as it's always possible to break a word of length 0.
        2. Iterate through string characters
            1. Iterate through the current slice
                1. If at some point dp is True and the rest of the slice is in wordDict -> make current dp also True.
        3. Return dp[-1]
        """    
        word = ''
        dp = [True] + [False] * len(s)
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]