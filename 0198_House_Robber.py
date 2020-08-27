class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        General idea: from dynamic programming. If dp[i] - max amount of money at the ith house.
        dp[0] = nums[0]
        dp[1] = max(num[0], num[1])
        dp[k] = max(dp[k-2] + nums[k], dp[k-1])
        
        prev1 stores dp[k-1], prev2 stores dp[k-2]
        1. Base case: array of nums is empty
        2. Initialze prev1, prev2 as zeros
        3. Iterate through nums. Update prev1, prev2
        4. Return prev1
        """
        if len(nums) == 0:
            return 0
        prev1, prev2 = 0, 0
        for num in nums:
            tmp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = tmp
        return prev1
        