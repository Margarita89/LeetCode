# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        General idea: store all values in a list
        1. Base case: empty list or 1 node -> return True
        2. Initialize empty list 'values'
        3. With while loop iterate through all nodes and append its' values to a list
        4. Return True if values equal to reversed values
        """
        if not head or not head.next:
            return True
        
        values = []
        while head:
            values.append(cur.val)
            head = head.next
        return values == values[::-1]