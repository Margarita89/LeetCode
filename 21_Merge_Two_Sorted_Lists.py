# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. Check if 1 of the lists is None
        2. Use dummy node to return dummy.next 
            as it's not clear where to start - from l1 or l2
        3. Use while loop to go through l1 and l2 
            until one of them is finished and cur pointer
        4. Point to that Node that it's not yet None
        5. Return dummy.next
        """
        if l1 is None: return l2
        if l2 is None: return l1
        
        dummy = cur = ListNode(0)
        cur1, cur2 = l1, l2
        
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 or cur2
        
        return dummy.next
        