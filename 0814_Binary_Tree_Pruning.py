# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """
        General idea: recursive approach
        1. Base case: if not root -> return False
        2. Check left and if there are no 1's there -> make it None
        3. Check right and if there are no 1's there -> make it None
        4. Return True if the value in current node is 1 or left, or right subtrees have 1
        """
        def CheckNode(root):
            if not root:
                return False
            if not CheckNode(root.left):
                root.left = None
            if not CheckNode(root.right):
                root.right = None
            return root.val == 1 or CheckNode(root.left) or CheckNode(root.right)
        
        return root if CheckNode(root) else None