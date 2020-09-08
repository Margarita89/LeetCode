# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        General idea: recursive approach that returns -1 if find unbalanced subtree or the height of the subtree
        1. Base case: not root -> return 0
        2. Get the left and right values recursively (either heights or -1)
        3. If any of them returned -1 or the difference in heights is larger than 1 -> return -1
        4. Return height: 1 + max of the heights of left and right subtrees
        """
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return 1 + max(left, right)
        
        return check(root) != -1
        
                
        