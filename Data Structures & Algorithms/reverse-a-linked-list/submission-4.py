# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
     # <-1<-1<-2<-3<-3
                   # p, c,n
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        return prev