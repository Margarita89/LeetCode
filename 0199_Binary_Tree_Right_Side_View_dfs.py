# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        General idea: use DFS with root and level
        1. Initialize empty list right_view 
        2. Start dfs with root, level=0
            1. Everything makes sence only if root is not None
                1. Check if the length of right_view is less than (level + 1) (checks if the level is already filled) -> append current root.val
                2. Start dfs for the right subtree (increase level by 1)
                3. Start dfs for the left subtree (increase level by 1)
        3. Return right_view
        """
        
        def dfs(root, level, right_view):
            if root:
                if len(right_view) < level + 1:
                    right_view.append(root.val)
                dfs(root.right, level + 1, right_view)
                dfs(root.left, level + 1, right_view)
                
        right_view = []
        dfs(root, 0, right_view)
        return right_view
        
    