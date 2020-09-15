class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        General idea: dynamic programming. dp[i] stores all possible sums that are equal to i.
        1. Sort candidates
        2. Initialize dp as a list of empty lists
        3. Iterate through dp
            1. Iterate through numbers
                1. If number is larger than i - there is no sum -> break
                2. Iterate through previous sums that are equal to (i-number)
                    1. If there are no sums or the current number is larger than the last in sum (important not to avoid repetitions) -> append to dp [sum + [current number]]
        """
        candidates.sort()
        dp = [[[]]] + [[] for i in range(target)]
        for i in range(1, target + 1):
            for number in candidates:
                if number > i: break
                for s in dp[i - number]:
                    if not s or number >= s[-1]: 
                        dp[i] += [s + [number]]
        return dp[target]
        