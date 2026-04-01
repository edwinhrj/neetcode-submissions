# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # travers both trees and append to a list
        # return boolean equated lists
        lst = []
        lst2 = []

        def dfs(curr, visited: List):

            # append None to list, to keep the semblance of structure!
            if not curr:
                visited.append(None)
                return

            # add curr to visited
            visited.append(curr.val)
            
            # recurse
            left = dfs(curr.left, visited)
            right = dfs(curr.right, visited)

            return visited
        
        return dfs(p, lst) == dfs(q, lst2)

        
            


        