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
        # add curr to list
        # use dictionary to store node to index of random
        
        # can create copy of LL without random by iterating, 
        # and appending to new list
        # iterate one last time to add random pointers
        old_list = []
        random_idx = {}
        new_list = []
        curr = Node(-1)
        new = curr
        while head:
            # create new ll
            curr.next = Node(head.val)
            curr = curr.next # head of new ll
            old_list.append(head)
            new_list.append(curr)
            head = head.next
    
        for n in old_list:
            # add to dictionary
            if n.random != None:
                random_idx[n] = old_list.index(n.random)
            else:
                random_idx[n] = None

        for i in range(len(new_list)):
            # idx of random pointer, only if have
            if random_idx[old_list[i]] != None:
                idx = random_idx[old_list[i]]
                # map random of new list to random of new list
                new_list[i].random = new_list[idx]

        return new.next

       