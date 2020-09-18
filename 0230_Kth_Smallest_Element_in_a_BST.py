# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        General idea: traverse a tree iteratively and return kth element
        1. Initialize empty stack
        2. Use while loop for stack and root
            1. Use another while loop for root
                1. Append root to stack and and move left until possible
            2. Pop from stack and if it’s kth – return root.val (here k - 1 as k is decreased at next step)
            3. Decrease k
            4. Move to right node
        """
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if k - 1 == 0:
                return root.val
            k -= 1
            root = root.right