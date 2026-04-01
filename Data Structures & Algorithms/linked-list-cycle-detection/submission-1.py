# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next:
            slow, fast = head, head.next
        else: 
            return False

        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow, fast = slow.next, fast.next.next
        return False



        