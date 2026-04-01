# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # account for if ll is empty
        curr = head
        if not curr:
            return curr
        
        array = []
        # add all nodes into list
        while curr:
            array.append(curr)
            curr = curr.next

        # use 2 pointer approach to solve
        l, r = 0, len(array) - 1
        while l < r:
            array[l].next = array[r]
            l += 1
            
            # in the event when l move fwd, it lands 
            # on same node as r, we break it right now

            array[r].next = array[l]
            r -= 1
        array[l].next = None

        



        
        