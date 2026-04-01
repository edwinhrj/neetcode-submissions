# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        array = []

        # add all nodes into list
        while curr:
            array.append(curr)
            curr = curr.next

        # target node to remove is index [len-n]
        index = len(array) - n

        # ec: when remove index = 0,
        # js return next node
        if index == 0:
            return head.next

        # so we point prev to next node to remove
        prevNode = array[index-1]
        prevNode.next = prevNode.next.next
        
        return array[0]


        