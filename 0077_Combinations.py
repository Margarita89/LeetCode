class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        General idea: use backtracking, decrease k and update starting index 'first'
        1. Base case: k is 0 -> append current combination stores in stack to ans
        2. Iterate through array starting from first
            - recursively append current element to combination, decrease k and make starting index next to current element
        """
        ans = []
        
        def backtrack(nums, stack, k, first=0):
            if k == 0:
                ans.append(stack)
            for i in range(first, len(nums)):
                backtrack(nums, stack + [nums[i]], k-1, i+1)
            
        backtrack(range(1, n+1), [], k, 0)
        return ans
        

                
        