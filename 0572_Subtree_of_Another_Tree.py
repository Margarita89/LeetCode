# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    General idea: use recursion
    1. Method compare (recursive): 
        - base cases: s or t are None
        - return recursive answer if nodes are the same and subtrees are the same
    2. Method traversing (recursive):
        - return True is s is not None and then check 3 options:
            - s and t are the same -> method compare
            - t is subtree of s.left -> method traversing
            - t is subtree of s.right -> method traversing
    PS. t is not empty
    """
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traversing(s, t)
    
    def compare(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.compare(s.left, t.left) and self.compare(s.right, t.right)
    
    def traversing(self, s, t):
        return s is not None and (self.compare(s, t) or self.traversing(s.left, t) or self.traversing(s.right, t))
        