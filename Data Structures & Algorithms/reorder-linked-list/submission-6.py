# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []
        curr = head
        while curr:
            lst.append(curr)
            curr = curr.next
        
        # 2 pointer
        l, r = 0, len(lst) - 1
        res = ListNode(0)
        curr = head
        while l < r:
            curr.next = lst[r]
            l += 1
            curr = curr.next
            curr.next = lst[l]
            r -= 1
            curr = curr.next
        curr.next = None



            
        
        
        





                
            
            
            
        