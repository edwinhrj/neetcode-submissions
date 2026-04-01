# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if head.next == None:
            return None
        
        # add nodes to list o(n)
        lst = []
        while head:
            lst.append(head)
            head = head.next

        # index to be removed
        idx = len(lst) - n

        # remove node
        if idx != 0:
            nxt = lst[idx].next
            lst[idx - 1].next = nxt
        else:
            return lst[1]
    
        return lst[0]