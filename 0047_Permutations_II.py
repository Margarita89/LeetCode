class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        General idea: use recursion (backtracking) on the sorted array.
        1. Sort array of nums
        2. Start backtrack method with sorted array and 0 - a starting index
            1. Base case: starting index 'first' is the lase -> append array to result
            2. Iterate from starting index
                1. If current element is the same as first -> skip because this has been already calculated
                2. Swap 2 elements in array - ith and first 
                3. Start recursively with new array and first+1
        Don't forget to pass list(nums), not the reference to nums
        """
        def backtrack(nums, first=0):
            if first == len(nums) - 1:
                res.append(nums)
            for i in range(first, len(nums)):
                if i > first and nums[i] == nums[first]:
                    continue
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(list(nums), first+1)
        
        res = []
        nums.sort()
        backtrack(nums, 0)
        return res
        
        
        