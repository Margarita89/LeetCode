# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        General idea: use recursion to calculate maximum sums in left and right branch respectively and update max_sum. So, each node will be checked for being the parent-node of left and right branches.
        1. Initialize max_sum as minimum
        2. Recursive helper function to get the maximum sum in a branch:
            1. Base case: not root -> return 0
            2. Get left and right sums recursively
            3. If left or right are not positive, there is no sense of adding them -> make them 0
            4. Update max_sum as max from previous max_sum and path with current root as parent
            5. Return max of left and right branches
        3. Start recursive helper from root
        4. Return max_sum
        """
        self.max_sum = float('-inf')
        def helper(root):
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            self.max_sum = max(max_sum, left + root.val + right.val)
            return max(left, right) + root.val
        
        helper(root)
        return max_sum
        