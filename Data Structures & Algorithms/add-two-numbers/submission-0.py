# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1)
        final = prev
        carry = 0

        while l1 or l2 or carry:
            total = 0
            if l1 != None:
                total += l1.val
            if l2 != None:
                total += l2.val
            total += carry
            newVal = total % 10
            carry = total // 10
            prev.next = ListNode(newVal) # add into LL
            prev = prev.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        return final.next


        