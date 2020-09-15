class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        General idea: if the current total sum is negative – make the current element the total sum (there is no sense in adding current element to total sum if it’s negative – it would not make the sum max possible)
        1. Initialize max_sum and tot_sum as nums[0]
        2. Iterate through nums starting from the second element
            1. If tot_sum is negative -> just make it equal to current number
            2. Else: add current number to tot_sum
            3. Update max_sum as max from max_sum and tot_sum
        3. Return max_sum
        """
        max_sum = tot_sum = nums[0]
        for i in range(1, len(nums)):
            if tot_sum < 0:
                tot_sum = nums[i]
            else:
                tot_sum += nums[i]
            max_sum = max(max_sum, tot_sum)
        return max_sum
        