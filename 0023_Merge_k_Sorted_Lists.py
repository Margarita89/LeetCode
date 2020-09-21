# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        General idea: merge lists by pairs
        1. merge2lists:
            1. Initialize dummy node 0 and pointer cur to it
            2. Use while loop to iterate through 2 lists
                1. If value in list1 is less than in list2 -> point cur.next to list1 and move list1 pointer
                2. Else -> point cur.next to list2 and move list2 pointer
            3. If not list1 -> point cur.next to list2
            4. If not list2 -> point cur.next to list1
            5. Return head.next (remove dummy node 0)
            
        2. Base cases: only one element or empty list
        3. Initialize step = 1
        4. Use while loop until step will exceed len(lists) which will mean all merged lists are already in lists[0]
            1. Iterate through lists with step * 2 (for first interation - take every 2 lists)
                1. merge 2 lists (current and list in step distance) and write the result in current 
            2. Update step by multiplying by 2 (now every 2, 4 .. lists are merged together)
        5. Return lists[0]
        """
        def merge2lists(list1, list2):
            head = ListNode(0)
            cur = head
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
                cur = cur.next
            cur.next = list1 or list2
            return head.next
        
        
        if len(lists) == 1:
            return lists[0]
        
        if not lists:
            return None
        
        step = 1
        while len(lists) > step:
            for i in range(0, len(lists)-step, step * 2):
                lists[i] = merge2lists(lists[i], lists[i + step])
            step *= 2
        return lists[0]