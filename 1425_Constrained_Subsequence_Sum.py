from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        General idea: change nums as dp[i] = max(0, dp[i-k] .. dp[i-1]) + nums[i] - max sum with current element. Use decreasing stack
        1. Initialize empty deque
        2. Iterate through array
            1. Add q[0] to nums[i] so it will get the max of previous sums
            2. Remove all smaller sums from q
            3. Append nums[i] to q if it's not negative
            4. Use while loop for q to remove elements that are outside window. Attention: important to check q[0] == nums[i-k] because there might be no elements to remove already
        3. Return max(nums)
        """
        q = deque()
        for i in range(len(nums)):
            nums[i] += q[0] if q else 0  # make nums[i] current max using it
            while q and nums[i] > q[-1]:  # decreasing deque -> make sure q[0] is max
                q.pop()
            if nums[i] > 0:  # don't need to append negatives
                q.append(nums[i])
            while q and i >= k and q[0] == nums[i-k]:  # keep the window of size <= k
                q.popleft()
        return max(nums)