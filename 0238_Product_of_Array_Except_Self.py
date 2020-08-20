class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        General idea: store product going left to right and then update it going right to left
        1. Initialize output list with all 1's
        2. Iterate through nums from 1st index -> left to right direction
            1. Store in output product of previous with previous in nums
            Example: nums = [1,2,3,4]
                    output = [1,1,2,6]
        3. Iterate through nums from 1st index -> right to left direction 
            1. Store a product from right side in 'r' and multiply values in output by 'r'.
            2. Update r by multiplying by current value in nums
            Example: output = [1,1,2,6], r = 1
                     output = [1,1,2,6], r = 4
                     output = [1,1,8,6], r = 12
                     output = [1,12,8,6], r = 24
                     output = [24,12,8,6], r = 24
        4. Return output
        """
        output = [1] * len(nums)
        for i in range(1, len(nums)):
            output[i] = output[i-1] * nums[i-1]
            
        r = 1
        for i in reversed(range(len(nums))):
            output[i] *= r
            r *= nums[i]
            
        return output
        