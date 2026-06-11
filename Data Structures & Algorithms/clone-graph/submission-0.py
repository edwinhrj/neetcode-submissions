"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # for deep copy questions, always
        # use a hash map to map old -> new!

        # dfs to traverse the graph, hashmap to map old to new
        oldToNew = {} # this can be like our visited set
        def dfsAndClone(node):
            if node in oldToNew:
                return oldToNew[node] # return its copy if already made
            
            # else make a copy
            copy = Node(node.val)
            oldToNew[node] = copy # make copy + "add as marked"
            
            # loop thru neighbors like dfs + link copy with its copy neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfsAndClone(nei))

            return copy
        
        if not node:
            return None
            
        dfsAndClone(node)

        return oldToNew[node]



