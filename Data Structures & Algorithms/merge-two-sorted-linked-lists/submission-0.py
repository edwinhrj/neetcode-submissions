# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        saved = dummy
        node1 = list1
        node2 = list2
        while node1 and node2:
            if node1.val <= node2.val:
                dummy.next = node1
                dummy = dummy.next
                node1 = node1.next
            elif node1.val > node2.val:
                dummy.next = node2
                dummy = dummy.next
                node2 = node2.next
        
        if node1:
            # add to res ll
            dummy.next = node1
        if node2:
            # add to res ll
            dummy.next = node2

        return saved.next

        