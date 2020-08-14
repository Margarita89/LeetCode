class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        General idea: use recursion (backtracking) with an array where 1 element at a time is subtracted and added to a path
        1. Base case: array is empty -> append path to answer
        2. Iterate through elements of array and start recursion moving each element from array to path
        """
        ans = []
        
        def recursive_permute(nums, path):
            if not nums:
                ans.append(path)
            for i in range(len(nums)):
                recursive_permute(nums[:i] + nums[i+1:], path + [nums[i]])
        
        recursive_permute(nums, [])
        return ans
        
        
        