from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        General idea: use bfs approach
        1. Base case: not root -> return empty list
        2. Initialize a deque with a tuple of root and current level == 0
        3. Initialize empty list for answer: zigzag 
        4. Use while loop for deque q not to be empty
            1. Popleft from q a node and current level
            2. Append node to zigzag (if new level -> append as new list, else -> append to last level)
            3. Append left and right nodes if exist
        5. Iterate through zigzag and reverse odd lists
        6. Return zigzag
        """
        if not root:
            return []
        q = deque([(root, 0)])
        zigzag = []
        while q:
            node, level = q.popleft()
            if len(zigzag) <= level:
                zigzag.append([node.val])
            else:
                zigzag[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1)) 
            if node.right:
                q.append((node.right, level + 1))
        for i in range(len(zigzag)):
            if i % 2 != 0:
                zigzag[i] = zigzag[i][::-1]
        return zigzag
                103. Binary Tree Zigzag Level Order Traversal