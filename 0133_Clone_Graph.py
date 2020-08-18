"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        General idea: use BFS approach and store visited nodes
        1. Check if not node -> return None
        2. Create a copy of a given node
        3. Initialize stack with [node] and a hashmap that relates node.val to node_copy
        4. Use while loop for q
            1. Pop a node from q
            2. Iterate through this node neighbors
                1. If neighbor is not in visited (check by its value):
                    1. Add it to visited by doing a copy
                    2. Append this neighbor to q
                2. Important: update neighbors of the node_copy. Regardless if it was visited or not as we need to do it in both directions.
        5. Return node_copy
        """
        if not node:
            return node
        node_copy = Node(node.val)
        visited = {node.val: node_copy}
        q = [node]
        while q:
            node = q.pop()
            for n in node.neighbors:
                if n.val not in visited:
                    visited[n.val] = Node(n.val)
                    q.append(n)
                visited[node.val].neighbors.append(visited[n.val])
        return node_copy
        