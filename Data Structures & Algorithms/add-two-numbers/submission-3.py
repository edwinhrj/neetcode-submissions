# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # think of ll as arithmetic addtion
        # 321 + 654 = 975
        # is basically 1 + 4 + carry over (0) = 5 in ones place
        # 2 + 5 + carry over (0) = 7 in ones place
        # 3 + 6 + carry over(0) = 9 in ones place
        # return 5 -> 7 -> 9 which is 975

        # 9 + 100 = 109
        # 9 -> 0 -> 1
        # 0 - 0 - 1
        # 9
        # 9 - 

        carry = 0
        prev = ListNode(-1)
        res = prev
        while l1 and l2:
            ones_place = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            prev.next = ListNode(ones_place)
            prev = prev.next
            l1, l2 = l1.next, l2.next
        
        # check if one other number still has value
        while l1:
            ones_place = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            prev.next = ListNode(ones_place)
            prev, l1 = prev.next, l1.next
        while l2:
            ones_place = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            prev.next = ListNode(ones_place)
            prev, l2 = prev.next, l2.next

        # check if carry still has value i.e., 9 + 9 = 18
        if carry:
            prev.next = ListNode(carry)

        return res.next


