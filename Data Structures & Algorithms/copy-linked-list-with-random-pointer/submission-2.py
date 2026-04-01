"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}
        # use dictionary to map old nodes to new copy nodes 
        # for fast access and linkage
        curr = head

        dummy = head # to return

        # add node and copy node to dict for fast reference
        while curr:
            oldToCopy[curr] = Node(curr.val, None, None)
            curr = curr.next

        curr = head
        # add linkages
        while curr:
            # map copy's next pointer to correct node
            oldToCopy[curr].next = oldToCopy[curr.next]

            # map copy's random pointer to correct node
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[dummy]
            


