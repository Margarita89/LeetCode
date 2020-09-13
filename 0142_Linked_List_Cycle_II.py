# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        General idea: use 2 pointers
        1. Base case: list is empty or only 1 node that points to None -> return None
        2. Use while loop and 2 pointers (slow and fast) to find where they will meet
        3. Else: fast pointer will point to None -> return None (there is no cycle)
        4. Move head while it won't meet with slow pointer 'p'. 'p' is already in the cycle and 'p' is required length away from the cycle beginning. So when 'p' and head meet - it will be the node where the cycle begins
        5. Return head
        """
        if not head or not head.next:
            return None
        p = p2 = head
        while p2 and p2.next:
            p = p.next
            p2 = p2.next.next
            if p == p2:
                break
        else:
            return None
        while head != p:
            p = p.next
            head = head.next
        return head