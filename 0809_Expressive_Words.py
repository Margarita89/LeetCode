class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        """
        General idea: use check function for each word. In check iterate through S and use pointer to point to chars in W. There are 2 main options. Either 2 chars are equal - move both pointers or not. In that case it's important to check if there are more than 3 equal characters in  S (together with previous which was already equal to char from W).
        1. Check(S, W)
            1. Initliaze index j for word W
            2. Iterate through S
                1. If W is not yet finished and chars in S and W are equal -> move j index
                2. Elif 3 chars in S using previous char are not all equal (compare to S[i] * 3) -> return False
            3. Return j == m which means that S, W are both checked 
        2. Return sum of check for all words
        """
        def check(S, W):
            j, n, m = 0, len(S), len(W)
            for i in range(n):
                if j < m and S[i] == W[j]: 
                    j += 1
                elif S[i - 1:i + 2] != S[i] * 3 and S[i - 2:i + 1] != S[i] * 3:  
                    return False
            return j == m
        
        return sum(check(S, W) for W in words)

