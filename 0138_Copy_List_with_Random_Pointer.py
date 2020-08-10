"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        1. Create a copy list inside original
        2. Copy random pointers
        3. Retrive the copied list and restore original list
        """
        cur = head      
        # copy cur each time and insert after cur
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = cur.next.next
        # copy random pointers
        cur = head
        while cur:
            if cur.random:  # check if it doesn't point to None
                cur.next.random = cur.random.next
            cur = cur.next.next
        # retrieve the copied list
        cur = head
        dummy = Node(0)
        
        copy_cur = dummy
        while cur:
            step = cur.next.next
            
            temp = cur.next
            copy_cur.next = temp
            copy_cur = temp
            
            # restore original list    
            cur.next = step
            cur = step
        
        return dummy.next
        
            