# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        General idea: find middle of the linked list and reverse second half
        1. Base case: empty list or 1 node -> return True
        2. Initialize slow and fast (2x speed) pointers
        3. With while loop find middle of the linked list (if 1->2->2->1 slow will point to first 2, if 1->2->3->2->1 slow will point to 3)
        4. Separate linked list in 2 halfs: slow points to None and second is initialized as a head of a second half list
        5. Reverse second half of the list using dummy node as a new head: 'reverse'. Now there are 2 linked lists as 2 halves and second is reversed - it's enough to check for equality of nodes to confirm palindrome
        6. With while loop iterate through linked lists
            1. If node values are not equal -> return False
            2. Move pointers in both linked lists to next
        7. Return True
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        
        reverse = None
        while second:
            tmp = second.next
            second.next = reverse
            reverse = second
            second = tmp
        while reverse:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True