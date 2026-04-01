# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # add LL to list to always have smth to reference
        lst = []
        while head:
            lst.append(head)
            head = head.next

        # 2 pointer 
        l, r = 0, len(lst) - 1
        while l < r:
            lst[l].next = lst[r]
            l += 1
            lst[r].next = lst[l]
            r -= 1

        lst[l].next = None

        
        


            
        
        
        





                
            
            
            
        