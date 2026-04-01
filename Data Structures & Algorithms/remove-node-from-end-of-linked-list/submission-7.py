# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head

        # add ll into list
        lst = []
        while head:
            lst.append(head)
            head = head.next
        
        # edge cases
        if len(lst) == 1 and n == 1:
            return None
        if len(lst) == n:
            return dummy.next
    
        # remove connection from idx - 1 to idx and idx to idx + 1
        idx = len(lst) - n
        if idx + 1 > len(lst) - 1:
            lst[idx - 1].next = None
        else:
            lst[idx - 1].next = lst[idx + 1]

        return dummy