class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        General idea: use addtional array of reversed nums. In both arrays update elements by multiplying by previous (if it's 0 not to propagate all zeros). So, each element of nums will be the subarrays product till this element including. Each element of reversed nums will be the subarrays product of nums starting from end till this element including. One of these arrays contains required Maximum Product.
        1. Initialize rev_nums as nums reversed
        2. Iterate through all elements starting from second.
            1. If previous element is not zero -> multiply current in nums by the previous
            2. If previous element is not zero -> multiply current in nums reversed by the previous
        3. Return max from nums and reversed nums
        """
        rev_nums = nums[::-1]
        for i in range(1, len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1]
            if rev_nums[i-1] != 0:
                rev_nums[i] *= rev_nums[i-1]
        return max(nums + rev_nums)
        
