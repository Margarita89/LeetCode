# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        """
        General idea: use recursion and a global counter
        1. Base case: root is None -> return 0
        2. Get the maximum length for the left and right subtrees recursively
        3. Update lengths if nodes are equal to the root.val (current node) -> add 1 (edge) or make 0
        4. Update counter as the max between counter itself and total path between left and right subtrees (sum)
        5. Return max from max left and max right paths
        Attention: edges are calculated, not nodes!
        """
        self.counter = 0
        
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            l = l + 1 if (root.left and root.left.val == root.val) else 0
            r = dfs(root.right)
            r = r + 1 if (root.right and root.right.val == root.val) else 0
            self.counter = max(self.counter, l + r)
            return max(l, r)
        
        dfs(root)
        return self.counter