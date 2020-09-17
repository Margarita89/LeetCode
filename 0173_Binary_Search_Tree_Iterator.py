# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    General idea: use inorder traversal and store results into a list. Also use counter to point to the index in the list
    """
    def __init__(self, root: TreeNode):
        self.inorder = []
        self.counter = -1
        self.inorder_traversal(root)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            self.inorder.append(root.val)
            self.inorder_traversal(root.right)
    
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.counter += 1
        return self.inorder[self.counter]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.counter != len(self.inorder)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()