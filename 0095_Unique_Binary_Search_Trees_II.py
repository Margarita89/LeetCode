# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        General idea: use recursion to run through start to end of the list of nodes. In recursion iterate through start to end, choose ith value as a root and all possible combinations (obtained recursively start to i-1) to be root.left and others – root.right
        1. Base case: if start > end -> return [None]
        2. If start == end -> return TreeNode[start]
        3. Initialize an empty list 'ans'
        4. Iterate through start to (end+1)
        5. Left is a list of possible trees using nodes (start, i – 1) - created recursively
        6. Right is a list of possible trees using nodes (i + 1, end) - created recursively
        7. Use 2 nested loops to iterate through left and right lists
            1. Make root a TreeNode(i)
            2. Make root.left and root.right from left and right lists of trees
            3. Append resulting tree to 'ans'
        8. Return 'ans'

        """
        def binary_trees(start, end):
            if start > end:
                return [None]
            if start == end:
                return [TreeNode(start)]
            ans = []
            for i in range(start, end + 1):
                left = binary_trees(start, i - 1)
                right = binary_trees(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        ans.append(root)
            return ans
        
        return binary_trees(1, n) if n > 0 else []
         
        
        