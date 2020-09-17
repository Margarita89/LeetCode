from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        General idea: use bfs and 2 deques. q will store nodes at each level
        1. Base case: not root -> return empty list
        2. Initialize deque 'q' with root and answering list: 'average_height'
        3. Use while loop for q
            1. Initialize empty deque tmp
            2. Initialize cur_values and count (sum and how many elements)
            3. Use while loop for q
                1. Popleft node from q
                2. Update cur_values and count
                3. Append node.left and node.right to tmp if they exist
            4. Make q = tmp - next level
            5. Append average of current level to the 'average_height'
            6. Return 'average_height'
        """
        if not root:
            return []
        q = deque([root])
        average_height = []
        while q:
            tmp = deque()
            cur_values, count = 0, 0
            
            while q:
                node = q.popleft()
                cur_values += node.val
                count += 1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            
            q = tmp
            average_height.append(cur_values / count)
        
        return average_height