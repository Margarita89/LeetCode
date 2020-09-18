class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        General idea: iterate once through array and store 2 first maximum numbers and their indexes
        """
        max1, max2 = float('-inf'), float('-inf')
        ind1, ind2 = 0, 0
        for i, num in enumerate(nums):
            if num > max1:
                max1, max2 = num, max1
                ind1, ind2 = i, ind1
            elif num > max2:
                max2 = num
                ind2 = i
        return (nums[ind1] - 1) * (nums[ind2] - 1)