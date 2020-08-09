# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Recursive solution
        1. Base case: if root is None -> return 0
        2. Get the max depth for the left and right subtrees recursively
        3. Return current max depth which is 1 (itself) plus
            max of left and right depths 
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
