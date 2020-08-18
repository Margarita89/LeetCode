# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        General idea: use BFS and deque to store the node and it's level as tuple
        1. If not root -> return []
        2. Initialize q - a deque with (root, level=0) and empty list right_view
        3. With while loop for q:
            1. Popleft from q
            2. If q is empty (current node is the last on the level => it's on the right side) or the node is level higher than the next in q (also means that it's on the right side)
            3. If there is left child -> append to q
            4. If there is right child -> append to q
        4. Return right_view
        """
        if not root:
            return []
        q = collections.deque([(root, 0)])
        right_view = []
        while q:
            node, level = q.popleft()
            if not q or q[0][1] - level > 0:
                right_view.append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return right_view