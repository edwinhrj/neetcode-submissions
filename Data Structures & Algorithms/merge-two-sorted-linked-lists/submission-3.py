# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1 == None and l2 == None:
            return l1

        dummy = ListNode(-1)
        result = dummy # variable to keep track of first node
        
        # while both list still has values
        while l1 and l2:
            if l1.val >= l2.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next
            else:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
        
        if l1 == None:
            dummy.next = l2
        if l2 == None:
            dummy.next = l1
        
        return result.next