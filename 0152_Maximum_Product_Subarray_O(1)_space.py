class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        General idea: Use pos and neg to store current product max and min which ends with current element
        1. Initialize pos and neg as will as Maximum Product as first element of nums
        2. Iterate through nums from second element:
            1. Update pos as max(num, pos * num, neg * num) and neg as min(num, pos * num, neg * num)
            2. Update Maximum Product so far
        3. Return Maximum Product
        """
        pos = neg = max_prod = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            pos, neg = max(num, pos * num, neg * num), min(num, pos * num, neg * num)
            max_prod = max(max_prod, pos)
        return max_prod
        
