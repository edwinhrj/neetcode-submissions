# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # same as merge 2 sorted ll, but iterate instead of hardcoding the comparison check

        # go through all ll nodes, looping thru the k ll each time
        
        new = ListNode(-1)
        res = new
        while lists:
            idx = 0
            curr = lists[idx]
            # loops thru lists and grabs the smallest head of ll
            for n in range(len(lists)):
                if lists[n].val <= curr.val:
                    curr, idx = lists[n], n
            
            new.next = curr
            new, curr = new.next, curr.next

            if curr == None:
                lists.pop(idx)
            else:
                lists[idx] = lists[idx].next 
        
        return res.next