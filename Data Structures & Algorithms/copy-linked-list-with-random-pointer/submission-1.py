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
        # if head is None; empty list
        if head == None:
            return head
        
        curr = head
        prev = Node(-1)
        nodeArray = []
        finalArray = []
        indexDict = {}

        # add all nodes to nodeArray
        while curr:
            nodeArray.append(curr)
            curr = curr.next

        # initialise dict to store index of all nodes 
        # for o(1) retrieval
        for i, n in enumerate(nodeArray):
            indexDict[n] = i

        # create new nodes into finalArray
        for i, n in enumerate(nodeArray):
            curr = Node(n.val, None)
            prev.next = curr
            finalArray.append(curr)
            prev = prev.next
        
        # add random pointer linkd in new nodes
        # and next links
        for i, n in enumerate(finalArray):
            if nodeArray[i].random == None:
                continue
            indexRandom = indexDict[nodeArray[i].random]
            n.random = finalArray[indexRandom]

        
        return finalArray[0]
        

            


        

        